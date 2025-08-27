from django.db import models

# Create your models here.

class MovieName(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
           
    
class Desc(models.Model):
    moviename = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.description
    
class Genre(models.Model):
    moviename = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    genre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.genre

class Duration(models.Model):
    moviename = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    duration = models.CharField(max_length=20)
    
    def __str__(self):
        return self.duration
    
class ReleaseDate(models.Model):
    moviename = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    releasedate = models.CharField(max_length=20)
    
    def __str__(self):
        return self.releasedate
    
class IMDB(models.Model):
    moviename = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    IMDB = models.CharField(max_length=20)
    
    def __str__(self):
        return self.IMDB

class RottenTomatoes(models.Model):
    moviename = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    rottentomatoes = models.CharField(max_length=20)
    
    def __str__(self):
        return self.rottentomatoes

class Language(models.Model):
    moviename = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    language = models.CharField(max_length=20)
    
    def __str__(self):
        return self.language
    
class Director(models.Model):
    moviename = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    director = models.CharField(max_length=20)
    
    def __str__(self):
        return self.director


class Actor1(models.Model):
    moviename = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    Actor1 = models.CharField(max_length=20)
    
    def __str__(self):
        return self.Actor1

class Actor2(models.Model):
    moviename = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    Actor2 = models.CharField(max_length=20)
    
    def __str__(self):
        return self.Actor2
    



    
class link(models.Model):
    moviename = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    link = models.CharField(max_length=500)
    
    def __str__(self):
        return self.link

class image(models.Model):
    moviename = models.ForeignKey(MovieName, on_delete=models.CASCADE)
    image = models.CharField(max_length=500)
    
    def __str__(self):
        return self.image
