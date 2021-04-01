from django.urls import path
from .views import api_get_users, api_register_user, api_delete_user

urlpatterns = [
    path("users/", api_get_users),
    path("register/", api_register_user),
    path("delete/<int:id>", api_delete_user),
]