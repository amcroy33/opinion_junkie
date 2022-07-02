from email import contentmanager, message
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from requests import post
from .models import Movie, Review, get_user_model
from django.contrib.auth.decorators import login_required

def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'home/index.html', context)

def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    context = {
        'movie': movie
    }

    return render(request, 'movie/detail.html', context)

def reviews(request, movie_id):

    movie = (Movie, movie_id)

    context = {
        'post': post
    }

    return render(request, 'reviews/reviews.html', context)


@login_required
def favorite(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    if request.user not in movie.users.all():

        movie.users.add(request.user)

    else:
        pass

    return JsonResponse({
        'Favorited': request.user in movie.users.all(),
    })