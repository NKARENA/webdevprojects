from django.db import models

# Create your models here.
class Movie(models.Model):
    releasedate = models.DateField()
    moviename = models.CharField(max_length=30)
    hero = models.CharField(max_length=30)
    IMDB = models.FloatField()