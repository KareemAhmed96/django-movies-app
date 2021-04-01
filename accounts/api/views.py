from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from django.contrib.auth.models import User


@api_view(["GET", ])
def api_get_users(request):
    # returns query_set
    users = User.objects.all()

    # to get the JSON object
    serializer = UserSerializer(instance=users, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST", ])
def api_register(request):
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