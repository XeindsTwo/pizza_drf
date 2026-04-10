from django.contrib import admin
from django.urls import path

from pizzas.views import PizzaList

urlpatterns = [
    path('pizzas/', PizzaList.as_view(), name='pizza-list'),
]
