from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie


class MovieView(ListView):
    """Movie list"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movie/base.html'


class MovieDetailView(DetailView):
    """ Movie description"""
    model = Movie
    slug_field = "url"


