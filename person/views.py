from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from .serializers import PersonSerializer


# Create your views here.
class CreateView(generics.CreateAPIView):
    name = 'person_create'

    def get_authenticators(self):
        return ()

    def get_permissions(self):
        return ()

    def get_serializer_class(self):
        return PersonSerializer


class LoginView(APIView):
    name = 'login'

    def get_permissions(self):
        return ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response(
                data={
                    'token': user.auth_token.key,
                }
            )
        else:
            return Response(
                data={
                    'error': '认证失败，请确认账号和密码是否正确',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )