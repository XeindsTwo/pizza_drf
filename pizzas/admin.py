from django.contrib import admin

from pizzas.models import Pizza


# Register your models here.
@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_filter = ['price']
    search_fields = ['name']