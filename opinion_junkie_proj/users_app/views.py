import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth import (
    authenticate, 
    login as django_login,
    logout as django_logout
    )

from django.contrib import messages

# Create your views here.
def register(request):

    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        form = request.POST

        username = form.get('username')
        password = form.get('password')

        new_user = User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, f'Welcome, {new_user.username}')

        django_login(request, new_user)

        return redirect('opinion_junkie_app:home')

def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        form = request.POST

        username = form.get('username')
        password = form.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:

            messages.error(request, 'Invalid Username or Password')
            return render(request, 'login.html')

        django_login(request, user)

        messages.success(request, f"Welcome {user.username}!")

        return render(request, 'login.html')