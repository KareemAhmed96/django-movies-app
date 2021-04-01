from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics

from movies.models import Movie
from .serializers import MovieSerializer


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


@api_view(["PUT", "POST"])
def update(request, id):
    movie = Movie.objects.get(id=id)
    serializer = MovieSerializer(data=request.data, instance=movie)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "id": serializer.data["id"],
            "message": "Movie edited successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


# Generic Views

class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class CreateMovie(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class UpdateMovie(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class DeleteMovie(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Combined APIs

# class MovieRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

# viewsets
