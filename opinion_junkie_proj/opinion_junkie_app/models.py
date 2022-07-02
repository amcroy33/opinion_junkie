from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    poster_url = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.title}"

class Review(models.Model):
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews')
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

    def __str__(self):
        return f"{self.movie} - {self.pub_date}"