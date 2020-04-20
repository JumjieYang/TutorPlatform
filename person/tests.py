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
        url = reverse('login')
        data = {
            'username': 'testUser',
            'password': 'qwerty'
        }
        self.client.post(url, data=data)
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)


