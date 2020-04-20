from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from person.serializers import UserSerializer


# Create your views here.

class RegisterView(generics.CreateAPIView):
    name = 'person_create'

    def get_authenticators(self):
        return ()

    def get_permissions(self):
        return ()

    def get_serializer_class(self):
        return UserSerializer


class LoginView(ObtainAuthToken):
    name = 'login'

    def get_permissions(self):
        return ()

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                data={
                    'token': token.key,
                    'username': user.username,
                    'user_id': user.id
                }
            )
        else:
            return Response(
                data={
                    'error': 'Login failed',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

class LogoutView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status = status.HTTP_200_OK)
