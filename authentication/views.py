from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Role
from .serializers import UserSerializer, RoleSerializer

class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoleListAPIView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer