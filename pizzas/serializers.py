from rest_framework import serializers
from .models import Pizza
from decimal import Decimal

class PizzaSerializer(serializers.ModelSerializer):
    price_with_discount = serializers.SerializerMethodField()

    class Meta:
        model = Pizza
        fields = ['id', 'name', 'price', 'price_with_discount']

    def get_price_with_discount(self, obj):
        return float(obj.price) * 0.9