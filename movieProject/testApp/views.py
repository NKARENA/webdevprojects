from django.shortcuts import render
from testApp import forms
from testApp.models import Movie

# Create your views here.
def home(request):
    return render(request, 'testAppTem/index.html')
def add_movies(request):
    form = forms.MovieForm()
    if request.method == 'POST':
        form = forms.MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return home(request)
    return render(request, 'testAppTem/add.html', {"form":form})
def list_view(request):
    movie_list = Movie.objects.all()
    print(movie_list)
    return render(request, 'testAppTem/display.html', {"movie_list":movie_list})

