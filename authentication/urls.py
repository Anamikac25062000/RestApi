from django.urls import path
from .views import UserRegistrationAPIView, RoleListAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('roles/', RoleListAPIView.as_view(), name='role-list'),
]