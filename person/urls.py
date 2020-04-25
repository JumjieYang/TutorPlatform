from django.urls import path
from .views import *


urlpatterns = ([
    path('users/<int:pk>',UserDetailView.as_view(),name='user_detail'),
    path('profiles/', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(),name='read_profile')
])