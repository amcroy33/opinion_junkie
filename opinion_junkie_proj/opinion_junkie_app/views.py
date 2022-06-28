from email import contentmanager
from django.shortcuts import get_object_or_404, render
from requests import post
from .models import Movie, Review

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

def reviews(request, title):

    movie = (Movie, title)

    context = {
        'post': post
    }

    return render(request, 'reviews/reviews.html', context)