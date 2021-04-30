from django import template
from myapp.models import Category, Genre, Movie

register = template.Library()

@register.simple_tag()
def get_categories():
    #Afisare categorii
    return Category.objects.all()

@register.simple_tag()
def get_genres():
    # Afisare genuri
    return Genre.objects.all()

@register.inclusion_tag('myapp/tags/last_movies.html')
def get_last_movies():
    #afisarea ultimelor n filme adaugate
    movies = Movie.objects.order_by('-id')[:8]
    return {"last_movies": movies}

