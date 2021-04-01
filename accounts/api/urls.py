from django.urls import path
from .views import api_get_users, api_register

urlpatterns = [
    path("users/", api_get_users),
    path("register/", api_register),
]