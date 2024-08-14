from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import MovieName, Actor1, Actor2, Desc, Duration, Director, Genre, IMDB, Language, ReleaseDate, RottenTomatoes
from .forms import NewMovie

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def moviebase(response, id):
    mn = MovieName.objects.get(id=id)
    return render(response, "main/movie.html", {"mn":mn})

def addmovie(response):
    if response.method == "POST":
        form = NewMovie(response.POST)
         
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = MovieName(name=n)
            t.save()  
             
        return HttpResponseRedirect("form/%i" %t.id)     
    
    else:    
        form = NewMovie()
        
    return render(response, "main/addmovie.html", {"form":form})


def index(response, id):
    mn = MovieName.objects.get(id=id)
    
    if response.method == "POST":
        if response.POST.get("addmovie"):
            d = response.POST.get("des")
                    
        if len(d) > 2:
            mn.desc_set.create(description=d)
        else:
            print("Invalid")
        
            
    return render(response, "main/TRAIL.html", {"mn":mn}) 