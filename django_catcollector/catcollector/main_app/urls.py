#imports path function that will be used to define each route
from django.urls import path
from . import views

#list that will hold each route
urlpatterns = [
    #home route
    path('', views.home, name='home'),
    #about page route
    path('about/', views.about, name='about'),
    #view all cats route
    path('cats/', views.cats_index, name='index'),
]