from course.models import Course, ShoppingCart
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    courseList = CourseSerializer(many=True)
    class Meta:
        model = ShoppingCart
        fields = '__all__'
