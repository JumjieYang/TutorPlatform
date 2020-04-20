from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


# Create your tests here.
class Test_auth(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testUser', password='qwerty')

    def test_create_user(self):
        """
        Ensure we can create an user
        """
        url = reverse('register')
        data = {
            'username': 'testUser1',
            'password': 'testPassword'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='testUser1').username, 'testUser1')

        """
        Try to Create another user with same data, should raise Error
        """
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        response = response.json()
        self.assertEqual(response['username'], ["A user with that username already exists."])

    def test_login_user(self):
        """
        ensure we can login an user
        """
        url = reverse('login')
        data = {
            'username': 'testUser',
            'password': 'qwerty'
        }
        response = self.client.post(url, data=data)
        response = response.json()

        token = Token.objects.get(user=self.user)
        self.assertEqual(response['token'],token.key)
        self.assertEqual(response['username'],self.user.username)
        self.assertEqual(response['user_id'],self.user.id)

    def test_login_user_wrong_password(self):
        url = reverse('login')
        """
        Try login with wrong password
        """
        data = {
            'username': 'testUser',
            'password': 'qwert'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        response = response.json()
        self.assertEqual(response['error'],"Login failed")

    def test_logout_user(self):
        url = reverse('login')
        data = {
            'username': 'testUser',
            'password': 'qwerty'
        }
        self.client.post(url, data=data)
        token = Token.objects.get(user=self.user)
        self.assertIsNotNone(token)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        try:
            Token.objects.get(user=self.user)
        except Exception as e:
            self.assertEqual('Token matching query does not exist.',e.__str__())
        finally:
            """
            Try to logout again, should raise 401 status code
            """
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
            response = response.json()
            self.assertEqual(response['detail'], "Invalid token.")
