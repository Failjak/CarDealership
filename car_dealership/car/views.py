from rest_framework import mixins
from rest_framework import viewsets

from .models import Car, CarPrices, CarConfiguration
from .serializer import CarSerializer, CarPricesSerializer, CarConfigSerializer


class CarViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class CarPricesViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = CarPricesSerializer
    queryset = CarPrices.objects.all()


class CarConfigViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = CarConfigSerializer
    queryset = CarConfiguration.objects.all()
