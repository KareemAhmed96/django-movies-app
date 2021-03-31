from django.contrib import admin
from .models import Movie, Category, Cast, Rate, Country

admin.site.site_url = 'http://localhost:8000/movies/'

class MovieInline(admin.StackedInline):
    model = Movie
    extra = 1
    max_num = 5


class CountryAdmin(admin.ModelAdmin):
    inlines = [MovieInline]


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'year')
    list_filter = ('year',)


# Register your models here.
admin.site.register(Movie, MoviesAdmin)
admin.site.register(Category)
admin.site.register(Rate)
admin.site.register(Country, CountryAdmin)
admin.site.register(Cast)
