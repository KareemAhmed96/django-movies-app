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
