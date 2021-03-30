from django import forms
from .models import Movie, Category


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

