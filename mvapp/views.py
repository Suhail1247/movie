from django.shortcuts import render, redirect
from .models import Movie
from .forms import mvform

# Create your views here.
def f1(request):
    mv= Movie.objects.all()
    return render(request,'home.html',{'movie':mv})
def detail(request,id):
    m=Movie.objects.get(id=id)
    return render(request,'details.html',{'movie':m})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        img=request.FILES['imgs']
        m=Movie(name=name,desc=desc,imgs=img)
        m.save()
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=mvform(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html', {'movie':movie,'form':form})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')

