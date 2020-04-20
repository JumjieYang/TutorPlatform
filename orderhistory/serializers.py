from rest_framework import serializers

from course.serializers import CourseSerializer
from .models import *


class OrderHistorySerializer(serializers.ModelSerializer):
    courseList = CourseSerializer(many=True)

    class Meta:
        model = OrderHistory
        fields = '__all__'
