from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View, TemplateView

from .models import Movie, Category, Actor, Genre
from .forms import ReviewForm, RattingForm


class GenreYear:

    def get_years(self):
        return Movie.objects.filter(draft=False).values_list("year",flat=True).distinct()

    def get_genres(self):
        return Genre.objects.all()


class HomeView(TemplateView):
    template_name = 'myapp/base.html'


class MovieView(GenreYear, ListView):
    """Movie list"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'myapp/movie_list.html'
    paginate_by = 4


class MovieDetailView(DetailView):
    """ Movie description"""
    model = Movie
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RattingForm()
        context["form"] = ReviewForm()
        return context


class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorDetailView(DetailView):
    #Actor information

    model = Actor
    template_name = 'myapp/actor.html'
    slug_field = "url"


class FilterMoviesView(GenreYear, ListView):

    # Aici se vor selecta filmele dupa an sau dupa gen, dar nu dupa an si dupa gen :)
    paginate_by = 4

    def get_queryset(self):

        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        return context


class Search(ListView):

    paginate_by = 3

    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context