from django.urls import path
from . import views
 
urlpatterns =  [

     path("",views.home, name="home"),
     path("Home",views.home, name="Home"),
     path("<int:id>",views.moviebase, name = "Base"),
     path("addmovie/",views.addmovie, name = "NewMovie"),
     path("addmovie/form/<int:id>",views.index, name = "INDEX"),
]


