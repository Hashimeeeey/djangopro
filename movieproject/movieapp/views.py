from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie

class MovieList(ListView):
    model = Movie
    template_name = "index.html"
    context_object_name = "movie_list"

class MovieDetail(DetailView):
    model = Movie
    template_name = 'detail.html'
    context_object_name = "movie"

class Movieadd(CreateView):
    model = Movie
    template_name = "bootstrap4/uni_form.html"
    fields = '__all__'  # Fix the typo here
    success_url = reverse_lazy('movieapp:index')

class Movieupdate(UpdateView):
    model = Movie
    template_name = "edit.html"
    fields = '__all__'
    success_url = reverse_lazy('movieapp:index')

class Moviedelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movieapp:index')
    template_name = 'delete.html'
