from django.contrib import admin
from .models import Movie, Category, Rate, Country

admin.site.site_url = 'http://localhost:8000/movies/'

# Register your models here.
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Rate)
admin.site.register(Country)
