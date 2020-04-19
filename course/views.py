from course.models import Course
from course.serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import  generics


class CourseCreateView(generics.CreateAPIView):
    def get_serializer_class(self):
        return CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

