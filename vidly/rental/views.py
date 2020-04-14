from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Movie


###  CRUD
#from .models import Movie
	
#Movie.objects.all()

#Movie.objects.filter(release_year=1994)

#Movie.objects.get(id=1)

#def index(request):  
#   return HttpResponse("Hello World! You're at the rental index")


def index(request):
    movies = Movie.objects.all()
    return render(request, 'views/index.html', { 'movies': movies } )

def details(request, movie_id):  
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'views/details.html', { 'movie': movie } )


# def index(request):
#     my_dict = {"insert_me": "I am from views.py"}
#     return render(request, 'views/index.html',context=my_dict)
    

