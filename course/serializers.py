from course.models import Course, ShoppingCart
from rest_framework import serializers

from person.models import Profile



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'

