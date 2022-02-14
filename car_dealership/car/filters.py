from datetime import datetime

import django_filters
from django_filters import rest_framework as filters
from .models import Car, CarPrices, CarConfiguration


class CarFilter(filters.FilterSet):
    class Meta:
        model = Car
        fields = {
            'brand': ['icontains', 'exact'],
            'model': ['icontains', 'exact'],
        }


class CarPriceFilter(filters.FilterSet):
    class Meta:
        model = CarPrices
        fields = {
            'car__brand': ['icontains', 'exact'],
            'price': ['gte', 'lte'],
        }


class CarConfigurationFilter(filters.FilterSet):
    start_release = django_filters.DateFilter(field_name='release_year', lookup_expr=('lt'))
    end_release = django_filters.DateFilter(field_name='release_year', lookup_expr=('gt'))

    class Meta:
        model = CarConfiguration
        fields = {
            'car__brand': ['icontains', 'exact'],
        }
