from rest_framework import serializers
from Backend.models import *

class UserSerializer(serializers.Serializer):
    
    def create(self, validated_data):
        """
        