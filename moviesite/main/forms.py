from django import forms

class NewMovieForm(forms.Form):
    title = forms.CharField(label="Movie Title", max_length=200)
    description = forms.CharField(widget=forms.Textarea, label="Description")
    genre = forms.CharField(max_length=100)
    duration = forms.CharField(max_length=20)
    release_date = forms.CharField(max_length=20)
    imdb_rating = forms.CharField(max_length=20)
    rottentomatoes_rating = forms.CharField(max_length=20)
    language = forms.CharField(max_length=20)
    director = forms.CharField(max_length=100)
    actors = forms.CharField(label="Actors (comma-separated)")
    poster = forms.ImageField()
    trailer_link = forms.URLField(max_length=500)