from django.urls import path

from .views import *

urlpatterns = [
    path('orders/', OrderList.as_view()),
    path('order/<int:pk>', OrderDetail.as_view()),
]

