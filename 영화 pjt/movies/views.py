from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie, Comment

# Create your views here.
def index(request):
    movies = Movie.objects.all
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, pk):
    movie = Movie.objects.field(pk=pk)
    commentform = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comment_form': commentform,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)