from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


# Create your tests here.
class Test_person(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testUser', password='qwerty')
        self.user1 = User.objects.create_user(username='testUser1', password='qwert')
        self.url = reverse('login')
        self.data = {
            'username': 'testUser',
            'password': 'qwerty'
        }
        self.profile_data = {
            'user': 1,
            'firstName': 'john',
            'lastName': 'doe',
            'age': 20,
            'phoneNumber': '123456789'
        }
        self.client.post(self.url, data=self.data)
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_user(self):
        url = reverse('user_detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = response.json()
        self.assertEqual(response['username'], 'testUser')
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = response.json()

    def test_get_user_no_auth(self):
        url = reverse('user_detail', args=[1])
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = response.json()
        self.assertEqual('Authentication credentials were not provided.', response['detail'])

    def test_get_user_not_self(self):
        url = reverse('user_detail', args=[2])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = response.json()
        self.assertEqual('Not found.', response['detail'])

    def test_modify_user(self):
        url = reverse('user_detail', args=[1])
        data = {
            'username': 'testUser',
            'password': 'asdfgh'
        }
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = response.json()
        self.assertEqual('Please login again', response['message'])
        self.assertEqual('testUser', response['username'])
        try:
            Token.objects.get(user=self.user)
        except Exception as e:
            self.assertEqual('Token matching query does not exist.', e.__str__())

    def test_partial_update_user(self):
        url = reverse('user_detail', args=[1])
        data = {
            'username': 'testUser',
            'password': 'asdfgh'
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = response.json()
        self.assertEqual('Please login again', response['message'])
        self.assertEqual('testUser', response['username'])
        try:
            Token.objects.get(user=self.user)
        except Exception as e:
            self.assertEqual('Token matching query does not exist.', e.__str__())

    def test_delete_user(self):
        url = reverse('user_detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        try:
            User.objects.get(username='testUser')
        except Exception as e:
            self.assertEqual("User matching query does not exist.", e.__str__())

    def test_profile(self):
        url = reverse('create_profile')
        response = self.client.post(url, data=self.profile_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = response.json()
        self.assertEqual(response['user'], self.user.id)
        self.assertEqual(response['firstName'], 'john')
        self.assertEqual(response['lastName'], 'doe')
        self.assertEqual(response['age'], 20)
        self.assertIsNone(response['image'])
        self.assertEqual(response['phoneNumber'], '123456789')
        url = reverse('read_profile', args=[1])
        """
        Test read profile
        """
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response = response.json()
        self.assertEqual(response['user'], self.user.id)
        self.assertEqual(response['firstName'], 'john')
        self.assertEqual(response['lastName'], 'doe')
        self.assertEqual(response['age'], 20)
        self.assertIsNone(response['image'])
        self.assertEqual(response['phoneNumber'], '123456789')
        """
        Test modify profile
        """
        self.profile_data['age'] = 25
        response = self.client.put(url, data=self.profile_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = response.json()
        self.assertEqual(response['user'], self.user.id)
        self.assertEqual(response['firstName'], 'john')
        self.assertEqual(response['lastName'], 'doe')
        self.assertEqual(response['age'], 25)
        self.assertIsNone(response['image'])
        self.assertEqual(response['phoneNumber'], '123456789')


