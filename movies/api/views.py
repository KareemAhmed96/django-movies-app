from rest_framework.response import Response
from rest_framework import status
from movies.models import Movie
from .serializers import MovieSerializer
from rest_framework.decorators import api_view


@api_view(["GET", ])
def index(request):
    # returns query_set
    movies = Movie.objects.all()

    # to get the JSON object
    serializer = MovieSerializer(instance=movies, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST", ])
def create(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "id": serializer.data["id"],
            "message": "Movie created successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)
