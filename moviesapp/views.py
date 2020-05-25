from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie, Artist, Genre, Rating
from .forms import ReviewForm, RatingForm


class GenreAndCountry:
    """Get Genres and Countries"""

    def get_genres(self):
        return Genre.objects.all()

    def get_countries(self):
        return Movie.objects.filter(draft=False).values("country")


class MoviesView(GenreAndCountry, ListView):
    """Movies list"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)
    paginate_by = 1
    template_name = "movies/movie_list.html"


class MovieDetailView(GenreAndCountry, DetailView):
    """Single Movie View"""

    model = Movie
    slug_field = "url"
    template_name = "movies/movie_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingForm()
        return context


class AddReview(View):
    """Review View"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
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
    paginate_by = 1

    def get_queryset(self):

        if self.request.GET.get("q", None):
            queryset = Movie.objects.filter(Q(country__in=self.request.GET.getlist("country")) |
                                            Q(genres__in=self.request.GET.getlist("genre")) |
                                            Q(title__icontains=self.request.GET.get("q")) &
                                            Q(draft=False)
                                            ).distinct().only("id", "title", "tagline", "poster").order_by("-id")
        else:
            queryset = Movie.objects.filter(Q(country__in=self.request.GET.getlist("country")) |
                                            Q(genres__in=self.request.GET.getlist("genre")) &
                                            Q(draft=False)
                                            ).distinct().only("id", "title", "tagline", "poster").order_by("-id")

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        context["country"] = ''.join([f"country={x}&" for x in self.request.GET.getlist("country")])
        return context


class AddStarRating(View):
    """Add rating to movie"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
