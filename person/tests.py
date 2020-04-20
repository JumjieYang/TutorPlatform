from django.contrib.auth.models import User
from django.test import TestCase
import requests


# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:8000/api-user/'
        self.username = 'testUser'
        self.password = 'qwerty'
        self.param = {
            'username': self.username,
            'password': self.password
        }
        self.token = requests.post(self.base_url + 'login/', data=self.param)
        self.headers = {
            ''
        }

    def tearDown(self):
        pass

    def test_create_user(self):
        data = {
            'username': 'testUser2',
            'password': 'qwerty'
        }
        r = requests.post(self.base_url + 'register/', data=data)
        result = r.json()

        self.assertEqual(result['username'], 'testUser2')

    def test_login_user(self):
        data = {
            'username': 'testUser',
            'password': 'qwerty'
        }
        r = requests.post(self.base_url + 'login/', data=data)
        result = r.json()
        self.assertIsNotNone(result['token'])
        self.token = result['token']
        self.assertEqual(result['username'], 'testUser')
        self.assertEqual(result['user_id'], 1)

    def test_get_user(self):
        r = requests.get(self.base_url + 'user/1', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'testUser')

    def test_update_user(self):
        data = {
            'id': 1,
            'username': 'testUser',
            'password': 'asdfgh'
        }
        r = requests.put(self.base_url + 'user/1', data=data, headers=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'testUser')

    def test_delete_user(self):
        data = {
            'id': 1
        }
        r = requests.delete(self.base_url + 'user/1', auth=self.auth)
        result = r.json()
