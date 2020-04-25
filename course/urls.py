from django.urls import path

from .views import *

urlpatterns = [
    path('course/', CourseCreateView.as_view(),name='course_create'),
    path('course/<int:pk>', CourseDetail.as_view(),name='course_detail'),
    path('courses/', CourseList.as_view(),name='course_all'),
    path('courses/<int:pk>', CourseList.as_view(),name='course_list'),
    path('carts/', CreateCart.as_view(),name='cart_list'),
    path('carts/', CartDetail.as_view(),name='cart_detail'),
]

