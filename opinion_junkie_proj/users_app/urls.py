from django.urls import path

from . import views

app_name = 'users_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('users/<str:username>', views.profile, name='profile')
]