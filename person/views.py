from rest_framework import generics
from rest_framework.response import Response

from .serializers import *


# Create your views here.


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        user = request.user
        user.set_password(request.data['password'])
        user.save()
        request.user.auth_token.delete()
        return Response(
            data={
                'username': user.username,
                'message': 'Please login again'
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
