from django.urls import path

from .views import *

urlpatterns = [
    path('pay/',PaymentView.as_view(),name='payment'),
]
