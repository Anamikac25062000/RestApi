from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role
 
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
 
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
 
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
 
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '_all_'