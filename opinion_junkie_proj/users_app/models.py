from django.db import models

from opinion_junkie_app.models import Movie

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    favorites = models.ManyToManyField(Movie, blank=True, related_name='users')

    def __str__(self):
        return self.username