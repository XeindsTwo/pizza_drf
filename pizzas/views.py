from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Pizza
from .serializers import PizzaSerializer


class PizzaList(ListAPIView):
    queryset = Pizza.objects.order_by('-price')
    serializer_class = PizzaSerializer


class PizzaCreate(CreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaDetail(RetrieveAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaUpdate(UpdateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class PizzaDelete(DestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
