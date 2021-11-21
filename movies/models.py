from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)
    genre_code = models.IntegerField()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    poster_path = models.CharField(max_length=200)
    popularity = models.FloatField()
    backdrop_path = models.CharField(max_length=200)
    # backdrop_path = models.TextField(null=True)
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="like_movies")

    def __str__(self):
        return self.title