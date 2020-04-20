from django.urls import path

from .views import *

urlpatterns = [
    path('orders/',OrderList.as_view(),name='order_list'),
    path('order/<int:pk>', OrderDetail.as_view(), name='order_detail'),
]

