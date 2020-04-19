from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import *


urlpatterns = ([
    path('register/', CreateView.as_view(), name=CreateView.name),
    path('login/', LoginView.as_view()),
])