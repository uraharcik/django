from django.utils.text import slugify
from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    """Categoriile de filme"""

    name = models.CharField("Category", max_length=50)
    description = models.TextField('Description')
    url = models.SlugField(max_length=100, unique=True, default=name)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField('Name', max_length=100)
    birth = models.DateField('Date of Birth')
    description = models.TextField('Description')
    img = models.ImageField('Image', upload_to='actors/')
    url = models.SlugField(max_length=100, unique=True, default='', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.url = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField("Category", max_length=50)
    description = models.TextField('Description')
    url = models.SlugField(max_length=100, unique=True, default='', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.url = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Movie(models.Model):
    title = models.CharField('Title', max_length=100)
    tagline = models.CharField('Tagline', max_length=100, default='')
    description = models.TextField('Description')
    poster = models.ImageField('Image', upload_to='movie/')
    year = models.DateField('Year')
    country = models.CharField('Conuntry', max_length=50)
    directors = models.ManyToManyField(Actor, verbose_name='Director', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='Actors', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='Genres')
    imdb_ratting = models.FloatField('iMDb Ratting', default=5)
    world_premiere = models.DateField('World Premiere', default=date.today)
    budget = models.PositiveIntegerField('Budget', default=0, help_text='Indicate in $')
    fees_in_usa = models.PositiveIntegerField('Fees in USA', default=0, help_text='Indicate in $')
    fees_in_world= models.PositiveIntegerField('Fees in world', default=0, help_text='Indicate in $')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=100, unique=True, blank=True, default='')
    draft = models.BooleanField('Draft', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={"slug": self.url})

    def save(self, *args, **kwargs):
        value = self.title
        self.url = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class MovieShots(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='movies_shot/')
    movies = models.ForeignKey(Movie, verbose_name='Movie', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class RattingStar(models.Model):
    value = models.SmallIntegerField('Value', default=0)

    def __str__(self):
        return self.value


class Ratting(models.Model):
    ip = models.CharField('IP adress', max_length=15)
    star = models.ForeignKey(RattingStar, on_delete=models.CASCADE, verbose_name='star')
    movie = models.ForeignKey(Movie, verbose_name='Movie', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.movie}"


class Reviews(models.Model):

    email = models.EmailField()
    name = models.CharField("Category", max_length=100)
    text = models.TextField('Description')
    parent = models.ForeignKey('self', verbose_name='Parent', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='Movie', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"