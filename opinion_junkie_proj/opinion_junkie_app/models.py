from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} - {self.release_date} - {self.genre}"

class Review(models.Model):
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    rating = models.DecimalField(
        default=0.0,
        validators= [
            MaxValueValidator(5.0),
            MinValueValidator(0.0)
        ],
        decimal_places=1,
        max_digits=2
    )