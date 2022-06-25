from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    # url = 

    def __str__(self):
        return self.title

class Review(models.Model):
    post = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    rating = models.DecimalField(
        default=3.0,
        validators= [
            MaxValueValidator(5.0),
            MinValueValidator(0.0)
        ],
        decimal_places=1,
        max_digits=2
    )