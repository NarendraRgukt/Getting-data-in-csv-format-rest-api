from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        exclude=("password",)

class DataSerializer(serializers.Serializer):
    field1=serializers.CharField()
    field2=serializers.CharField()
    
