from django.contrib import admin
from .models import MovieName, Actor1, Actor2, Desc, Duration, Director, Genre, IMDB, Language, ReleaseDate, RottenTomatoes, image, link
# Register your models here.


admin.site.register(MovieName)
admin.site.register(Actor1)
admin.site.register(Actor2)
admin.site.register(Desc)
admin.site.register(Director)
admin.site.register(Duration)
admin.site.register(Genre)
admin.site.register(IMDB)
admin.site.register(Language)
admin.site.register(ReleaseDate)
admin.site.register(RottenTomatoes)
admin.site.register(link)
admin.site.register(image)

