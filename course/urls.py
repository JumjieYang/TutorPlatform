from django.urls import path

from .views import *

urlpatterns = [
    path('create-course/', CourseCreateView.as_view()),
    path('courses/<int:pk>', CourseDetail.as_view()),
    path('courses/', CourseList.as_view()),
    path('create-cart/', CreateCart.as_view()),
    path('carts/', CartDetail.as_view()),
]

