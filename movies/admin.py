from django.contrib import admin
from .models import Movie, Category, Rate, Country

# Register your models here.
admin.site.register(Movie, name="Movie")
admin.site.register(Category)
admin.site.register(Rate)
admin.site.register(Country)
