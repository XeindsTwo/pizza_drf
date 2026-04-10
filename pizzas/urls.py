from django.contrib import admin
from django.urls import path

from pizzas.views import PizzaList, PizzaCreate, PizzaDetail, PizzaUpdate, PizzaDelete

urlpatterns = [
    path('pizzas/', PizzaList.as_view(), name='pizza-list'),
    path('pizzas/', PizzaCreate.as_view(), name='pizza-create'),
    path('pizzas/<int:pk>', PizzaDetail.as_view(), name='pizza-detail'),
    path('pizzas/<int:pk>', PizzaUpdate.as_view(), name='pizza-update'),
    path('pizzas/<int:pk>', PizzaDelete.as_view(), name='pizza-delete'),
]