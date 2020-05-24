from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie, Artist, Genre
from .forms import ReviewForm


class GenreAndCountry:

    def get_genres(self):
        return Genre.objects.all()

    def get_countries(self):
        return Movie.objects.filter(draft=False).values("country")


class MoviesView(GenreAndCountry, ListView):
    """Movies list"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"

class MovieDetailView(GenreAndCountry, DetailView):
    """Single Movie View"""

    model = Movie
    slug_field = "url"
    template_name = "movies/movie_detail.html"


class AddReview(View):
    """Review View"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id = pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ArtistView(GenreAndCountry, DetailView):
    """Artist View"""
    model = Artist
    template_name = "movies/artist.html"
    slug_field = "name"


class FilterMoviesView(GenreAndCountry, ListView):
    """Film Filter"""

    template_name = "movies/movie_list.html"

    def get_queryset(self):
        queryset = Movie.objects.filter(Q(country__in=self.request.GET.getlist("country")) |
                                        Q(genres__in=self.request.GET.getlist("genre"))
                                        )

        return queryset


class JsonFilterMoviesView(GenreAndCountry, ListView):
    """Json Film Filter"""

    def get_queryset(self):
        queryset = Movie.objects.filter(Q(country__in=self.request.GET.getlist("country")) |
                                        Q(genres__in=self.request.GET.getlist("genre"))
                                        ).distinct().values("title", "tagline", "url", "poster")

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)
