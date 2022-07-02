from django import views
from django.urls import path
from . import views

app_name = 'opinion_junkie_app'
urlpatterns = [
    path('', views.home, name='myview'),
    path('home/', views.home, name='home'),
    path('detail/<int:movie_id>', views.detail, name='detail'),
    path('reviews/<int:movie_id>', views.reviews, name='reviews'),
    path('favorite/<int:movie_id>', views.favorite, name='favorite')
]