from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm

def index(request):
    movies = Movie.objects.all()
    return render(request,'movies/index.html',{'movies':movies})

def detail(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request,'movies/detail.html',{'movie':movie})
def addvideo(request):
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
        else:
            return HttpResponse('Invalid form')
    else:
        form = MovieForm()
    return render(request,'movies/addvideo.html',{'form':form})
def updatevideo(request,video_id):
    movie = get_object_or_404(Movie,pk=video_id)
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
        else:
            return HttpResponse('Invalid form')
    else:
        form = MovieForm(instance=movie)
    return render(request,'movies/addvideo.html',{'form':form})


def deletevideo(request,video_id):
    movie = get_object_or_404(Movie,pk=video_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    
    return HttpResponse('Opeees!')
    