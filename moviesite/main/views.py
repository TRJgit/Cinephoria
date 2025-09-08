from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Actor, Director
from .forms import NewMovieForm

# Create your views here.

def home(response):
    movies = Movie.objects.all().order_by('-id')
    latest_movie = movies.first()
    
    context = {
        'movies': movies,
        'latest_movie': latest_movie
    }
    return render(response, "main/home.html", context)

def moviebase(response, id):
    # Using get_object_or_404 is better practice to handle non-existent IDs gracefully
    movie = get_object_or_404(Movie, pk=id)
    return render(response, "main/movie.html", {"movie": movie})

def addmovie(response):
    if response.method == "POST":
        form = NewMovieForm(response.POST, response.FILES)
        if form.is_valid():
            # Create a new Movie object
            movie = Movie.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                genre=form.cleaned_data["genre"],
                duration=form.cleaned_data["duration"],
                release_date=form.cleaned_data["release_date"],
                imdb_rating=form.cleaned_data["imdb_rating"],
                rottentomatoes_rating=form.cleaned_data["rottentomatoes_rating"],
                language=form.cleaned_data["language"],
                poster=form.cleaned_data["poster"],
                trailer_link=form.cleaned_data["trailer_link"],
            )

            # Get or create the director
            director, created = Director.objects.get_or_create(name=form.cleaned_data["director"])
            movie.director = director

            # Get or create the actors
            actor_names = [name.strip() for name in form.cleaned_data["actors"].split(',')]
            for name in actor_names:
                actor, created = Actor.objects.get_or_create(name=name)
                movie.actors.add(actor)

            movie.save()
            return redirect("/")
    else:
        form = NewMovieForm()

    return render(response, "main/addmovie.html", {"form": form})