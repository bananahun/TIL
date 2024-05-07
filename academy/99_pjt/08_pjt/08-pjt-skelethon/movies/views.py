from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Genre, Movie


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/index.html', context)


def filter_genre(request, genre_pk):
    selected_movies = Genre.objects.get(pk=genre_pk)
    context = {
        'selected_movies': selected_movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def recommended(request):
    pass
