from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission

from .serializers import UserSerializer
from django.contrib.auth.models import User


# Custom permission
class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm("movies.view_movie")

@api_view(["GET", ])
def api_get_users(request):
    # returns query_set
    users = User.objects.all()

    # to get the JSON object
    serializer = UserSerializer(instance=users, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST", ])
def api_register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response(data={
                "success": False,
                "errors": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response(data={
            "success": True,
            "message": "User created successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE", ])
def api_delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return Response(data={
            "success": True,
            "id": id,
            "message": "User deleted successfully"
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response(data={
            "success": False,
            "errors": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
