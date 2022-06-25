from email import contentmanager
import re
from django.shortcuts import get_object_or_404, render
from .models import Movie

def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'home/index.html', context)

def detail(request, title):
    movie = get_object_or_404(Movie, title=title)

    context = {
        'movie': movie
    }

    return render(request, 'movie/detail.html', context)