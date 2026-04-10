from rest_framework.generics import ListAPIView
from .models import Pizza
from .serializers import PizzaSerializer

class PizzaList(ListAPIView):
    queryset = Pizza.objects.order_by('-price')
    serializer_class = PizzaSerializer