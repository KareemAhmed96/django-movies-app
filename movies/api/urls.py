from django.urls import path, include
from .views import index, create
from .views import MovieList, CreateMovie, UpdateMovie, DeleteMovie

urlpatterns = [
    path("", index),
    path("create", create),

    # generic urls
    path("generic/list/", MovieList.as_view()),
    path("generic/create/", CreateMovie.as_view()),
    path("generic/update/<int:pk>/", UpdateMovie.as_view()),
    path("generic/delete/<int:pk>/", DeleteMovie.as_view()),
]
