from django.urls import path
from .views import *


urlpatterns = ([
    path('users/<int:pk>',UserDetailView.as_view()),
    path('profiles/', CreateProfileView.as_view()),
    path('profile/<int:pk>/', ProfileDetailView.as_view())
])