from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.title)


class Cast(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField(max_length=500)

    def __str__(self):
        return str(self.name)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    year = models.DateField()
    rate = models.IntegerField()
    poster = models.ImageField(upload_to="movies/posters")
    video = models.FileField(upload_to="movies/video")
    categories = models.ManyToManyField(Category)
    cast = models.ManyToManyField(Cast)

    def __str__(self):
        return str(self.title)

