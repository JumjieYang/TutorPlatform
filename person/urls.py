from django.urls import path


from .views import *


urlpatterns = ([
    path('register/', CreateView.as_view(), name=CreateView.name),
    path('login/', LoginView.as_view(), name=LoginView.name),
])