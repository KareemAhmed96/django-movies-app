from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()

    return render(request, "movies/index.html", {
        'movies': movies
    })


def show(request, id):
    movie = Movie.objects.get(pk=id)

    return render(request, "movies/show.html", {
        'movie': movie
    })


def add(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request, "movies/add.html", {
        'form': form
    })


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


def delete(request, id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return redirect("index")

