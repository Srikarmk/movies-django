from django.http import HttpResponse
from django.shortcuts import render
data={
    'movies':[
        {
            'id':1,
            'title':'Wakanda Forever',
            'year':2022
        },
        {
            'id':2,
            'title':'Quantumania',
            'year':2023
        },
        {
            'id':3,
            'title':'Salaar',
            'year':2023
        }
    ]
}
def movies(request):
    return render(request,'movies/movies.html',data)
def homepage(req):
    return HttpResponse("Home Page")
