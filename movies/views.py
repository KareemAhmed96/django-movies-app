from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

@login_required
def index(request):
    movies = Movie.objects.all()

    return render(request, "movies/index.html", {
        'movies': movies
    })


@login_required
@permission_required("movies.view_movie")
def show(request, id):
    movie = Movie.objects.get(pk=id)

    return render(request, "movies/show.html", {
        'movie': movie
    })


@login_required
def add(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request, "movies/add.html", {
        'form': form
    })


@login_required
@permission_required("movies.edit_movie")
def edit(request, id):
    movie = Movie.objects.get(pk=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request, "movies/edit.html", {
        'form': form,
        'movie': movie
    })


@login_required
@permission_required("movies.delete_movie")
def delete(request, id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return redirect("index")

