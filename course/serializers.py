from course.models import Course, ShoppingCart
from rest_framework import serializers

from person.models import Profile


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('firstName','lastName','image')

class CourseSerializer(serializers.ModelSerializer):
    tutor = TutorSerializer(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'

