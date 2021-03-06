from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add, name="add"),
    path('show/<int:id>', views.show, name="show"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),
]
