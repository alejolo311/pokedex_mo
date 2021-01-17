  
from django.urls import path

from pokedex import views

urlpatterns = [
    path('pokemon/<str:name>', views.json, name="API"),
    path('pokemon/', views.all, name="pokedex")

]