from django.contrib import admin
from .models import Movie, Actor, Director

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    # This line adds a much better interface for selecting actors
    filter_horizontal = ('actors',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)
admin.site.register(Director)