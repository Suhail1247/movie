from django.shortcuts import render,HttpResponse
from .models import movie

# Create your views here.
def f1(request):
    m = movie.objects.all()
    return render(request,'home.html',{'movie':m})
def detail(request,movie_id):
    m=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':m})

