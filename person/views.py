from rest_framework import generics
from rest_framework.response import Response

from .serializers import *


# Create your views here.


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        return Response(
            data={
                'username': user.username
            }
        )

    def get_queryset(self):
        return self.queryset.filter(username=self.request.user)


class CreateProfileView(generics.CreateAPIView):
    def get_serializer_class(self):
        return ProfileSerializer


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
