from django.urls import path
from . import views

urlpatterns =  [
     path("",views.home, name="home"),
     path("<int:id>",views.moviebase, name = "Base"),
     path("addmovie/",views.addmovie, name = "NewMovie"),
]