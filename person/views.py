from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

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
                    'username': user.username
                }
            )
        else:
            return Response(
                data={
                    'error': 'Login failed',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )