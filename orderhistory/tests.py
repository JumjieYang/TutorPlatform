from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


# Create your tests here.
from course.models import Course, ShoppingCart
from orderhistory.models import OrderHistory


class Test_auth(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testUser', password='qwerty')
        self.course = Course.objects.create(subject="MATH", number=323, term='201909', description='test course')
        self.cart = ShoppingCart.objects.create(user=self.user,course=self.course)
        self.order = OrderHistory.objects.create(amount=0, address="hsdsds",owner=self.user, cart=self.cart)
        self.data = {
            'username': 'testUser',
            'password': 'qwerty'
        }
        self.client.post(reverse('login'), data=self.data)
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_order(self):
        url = reverse('order_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        response = response.json()[0]
        self.assertEqual(response['amount'],0)
        self.assertEqual(response['address'],'hsdsds')
        self.assertEqual(response['owner'],self.user.id)
        self.assertEqual(response['cart'],self.cart.id)

    def test_create_order(self):
        url = reverse('order_list')
        data = {
            'amount': 100,
            'address': 'sadd',
            'owner': self.user.id,
            'cart': self.cart.id
        }
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = response.json()
        self.assertEqual(response['amount'],100)
        self.assertEqual(response['address'], 'sadd')
        self.assertEqual(response['owner'], self.user.id)
        self.assertEqual(response['cart'], self.cart.id)

    def test_order_detail(self):
        url = reverse('order_detail', args=[1])
        data = {
            'amount': 1000
        }
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = response.json()
        self.assertEqual(response['amount'], 0)
        self.assertEqual(response['address'], 'hsdsds')
        self.assertEqual(response['owner'], self.user.id)
        self.assertEqual(response['cart'], self.cart.id)
        """
        modify amount
        """
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = response.json()
        self.assertEqual(response['amount'], 1000)
        self.assertEqual(response['address'], 'hsdsds')
        self.assertEqual(response['owner'], self.user.id)
        self.assertEqual(response['cart'], self.cart.id)

        """
        delete order
        """
        self.assertEqual(OrderHistory.objects.count(),1)
        self.client.delete(url)
        self.assertEqual(OrderHistory.objects.count(),0)
