from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from course.models import Course, ShoppingCart
from course.serializers import CourseSerializer


class Course_Test(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testUser', password='qwerty')
        self.course = Course.objects.create(subject="MATH", number=323, term='201909', description='test course')
        self.data = {
            'username': 'testUser',
            'password': 'qwerty'
        }
        self.client.post(reverse('login'), data=self.data)
        token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_course_create(self):
        url = reverse('course_create')
        data = {
            'subject': 'MATH',
            'number': 324,
            'term': '201909',
            'description': 'test course'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(Course.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = response.json()
        self.assertEqual(response['subject'], 'MATH')
        self.assertEqual(response['number'], 324)
        self.assertEqual(response['term'], '201909')
        self.assertEqual(response['description'], 'test course')
        self.assertEqual(response['time_chosed'], 0)
        self.assertFalse(response['isAvailable'])
        self.assertEqual(response['price'], 0)
        self.assertIsNone(response['tutor'], 0)

    def test_get_courses(self):
        self.client.credentials(HTTP_AUTHORIZATION='')
        url = reverse('course_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = response.json()
        course_json = CourseSerializer(self.course)
        self.assertEqual(response[0], course_json.data)

    def test_course_detail(self):
        """
        Retrieve a course
        """
        url = reverse('course_detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = response.json()
        course_json = CourseSerializer(self.course)
        self.assertEqual(response, course_json.data)

        """
        Update a course
        """
        data = {
            "tutor": 1
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = response.json()
        self.course.tutor = self.user
        course_json = CourseSerializer(self.course)
        self.assertEqual(response, course_json.data)

        """
        Delete a course
        """
        self.assertEqual(Course.objects.count(), 1)
        self.client.delete(url)
        self.assertEqual(Course.objects.count(), 0)

    def test_cart_create(self):
        url = reverse('cart_list')
        data = {
            'number': 1,
            'total': 50,
            'user': self.user.id,
            'course': self.course.id

        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        response = response.json()
        self.assertEqual(response['number'],1)
        self.assertEqual(response['total'],50)
        self.assertEqual(response['user'],self.user.id)
        self.assertEqual(response['course'],self.course.id)
        self.assertEqual(ShoppingCart.objects.count(),1)

    def test_get_carts(self):
        url = reverse('cart_list')
        data = {
            'user': 1,
            'course': self.course.id
        }
        self.client.post(url, data)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = response.json()[0]
        self.assertEqual(response['user'], self.user.id)
        self.assertEqual(response['course'], self.course.id)
        self.assertEqual(ShoppingCart.objects.count(), 1)

