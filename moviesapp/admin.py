from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Movie, MovieShots, Artist, Rating, RatingStar, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class MovieShotsInLine(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="150" height="100">')

    get_image.short_description = "Picture"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "url", "draft")
    list_display_links = ("title",)
    list_filter = ("category", "genres",)
    search_fields = ("title",)
    inlines = [MovieShotsInLine, ReviewInLine]
    save_on_top = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
           "fields": (("title","tagline"),)
        }),
        (None, {
            "fields": (("description", "poster", "get_image"),)
        }),
        (None, {
            "fields": (("running_time", "country"),)
        }),
        (None, {
            "fields": (("directors", "actors"),)
        }),
        (None, {
            "fields": ("genres", "world_premiere",)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        (None, {
            "fields": (("category", "url", "draft"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="150">')


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id","name", "email", "parent","movie",)
    list_display_links = ("name",)
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Picture"




@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="150" height="100">')

    get_image.short_description = "Picture"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "ip")


admin.site.register(RatingStar)

admin.site.site_title = "Адміністрування"
admin.site.site_header = "Адміністрування"
