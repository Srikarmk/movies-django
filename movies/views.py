from django.http import HttpResponse
from django.shortcuts import render
def movies(request):
    return render(request,'movies/movies.html',{'movies':['Wakanda Forever','Quantamania']})
def homepage(req):
    return HttpResponse("Home Page")
