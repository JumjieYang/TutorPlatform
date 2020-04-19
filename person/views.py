from django.contrib.auth import authenticate
from rest_framework import generics, status, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


# Create your views here.
class CreateUserView(generics.CreateAPIView):
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
            print(user)
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


class CreateProfileView(generics.CreateAPIView):
    def get_serializer_class(self):
        return ProfileSerializer

    permission_classes = [permissions.IsAuthenticated, ]


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
