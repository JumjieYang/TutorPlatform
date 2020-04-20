from django.urls import path

from .views import *

urlpatterns = [
    path('course/', CourseCreateView.as_view()),
    path('courses/<int:pk>', CourseDetail.as_view()),
    path('courses/', CourseList.as_view()),
    path('carts/', CreateCart.as_view()),
    path('carts/', CartDetail.as_view()),
]

