from django.shortcuts import render
from django.http import HttpResponse
from .models import cats

# Create your views here.
#home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡ꞈ｡ᐟ\</h1>')

#about view
def about(request):
    #returning a string response to the page when requesting the about page
    #return HttpResponse('<h1>About the CatCollector</h1>')
    return render(request, 'about.html')

def cats_index(request):
    return render(request, 'cats/index.html', { 'cats': cats })