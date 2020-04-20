from rest_framework import serializers

from course.serializers import CourseSerializer
from .models import *


class OrderHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHistory
        fields = '__all__'
