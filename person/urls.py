from django.urls import path
from .views import *


urlpatterns = ([
    path('register/', CreateUserView.as_view(), name=CreateUserView.name),
    path('login/', LoginView.as_view()),
    path('user/<int:pk>',UserDetailView.as_view()),
    path('profiles/', CreateProfileView.as_view()),
    path('profile/<int:pk>/', ProfileDetailView.as_view())
])