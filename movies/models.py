from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.title)


class Rate(models.Model):
    class Meta:
        verbose_name_plural = "Ratings"

    rate = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.rate)


class Cast(models.Model):
    class Meta:
        verbose_name_plural = "Cast"

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField(max_length=500)

    def __str__(self):
        return str(self.name)


class Country(models.Model):
    class Meta:
        verbose_name_plural = "Countries"

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Movie(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    year = models.DateField()
    poster = models.ImageField(upload_to="movies/posters")
    video = models.FileField(upload_to="movies/video")
    categories = models.ManyToManyField(Category)
    cast = models.ManyToManyField(Cast)
    rate = models.OneToOneField(Rate, null=True, on_delete=models.SET_NULL)

    # ForeignKey => One To Many Relation
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.title)

