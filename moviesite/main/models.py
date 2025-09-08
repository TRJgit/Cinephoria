from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    release_date = models.CharField(max_length=20)
    imdb_rating = models.CharField(max_length=20)
    rottentomatoes_rating = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True)
    actors = models.ManyToManyField(Actor)
    poster = models.ImageField(upload_to='posters/')
    trailer_link = models.URLField(max_length=500)

    def __str__(self):
        return self.title