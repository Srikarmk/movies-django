from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie
def movies(request):
    data = Movie.objects.all()
    return render(request,'movies/movies.html',{"movies":data})
def homepage(req):
    return HttpResponse("Home Page")
def detail(req,id):
    data=Movie.objects.get(pk=id)
    return render(req,'movies/detail.html',{'movie':data})
def add(req):
    title = req.POST.get('title')
    year=req.POST.get('year')
    if title and year:
        movie=Movie(title=title,year=year)
        movie.save()
        return HttpResponseRedirect('/movies')

    return render(req,"movies/add.html")
def delete(req,id):
    try:
        movie=Movie.objects.get(pk=id)
    except:
        raise Http404("Movie Not Found")
    movie.delete()
    return HttpResponseRedirect('/movies')
