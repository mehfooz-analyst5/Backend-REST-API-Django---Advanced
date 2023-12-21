"""
    Views for the user API
"""

from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
