from django.urls import path
from .views import api_get_users, api_register_user, api_delete_user
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("users/", api_get_users),
    path("login/", obtain_auth_token),
    path("register/", api_register_user),
    path("delete/<int:id>", api_delete_user),
]