from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('movie_list', views.MovieView.as_view(), name='movie_list'),
    path('filter/', views.FilterMoviesView.as_view(), name='movie_filter'),
    path('search/', views.Search.as_view(), name='search'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('actor/<slug:slug>/', views.ActorDetailView.as_view(), name='actor_detail'),
]