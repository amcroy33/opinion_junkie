from django import views
from django.urls import path
from . import views

app_name = 'opinion_junkie_app'
urlpatterns = [
    # path('myview/', views.myview, name='myview')
    path('', views.home, name='myview'),
    path('home/', views.home, name='home'),
    path('detail/<str:title>', views.detail, name='detail'),
    path('reviews/<str:title>', views.reviews, name='reviews')

]