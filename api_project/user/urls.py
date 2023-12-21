"""
    URL's mapping
"""

from django.urls import path, include
from user import views

urlpatterns = [
    path('create/', views.CreateUserView.as_view(),  name='create'),

 
]
