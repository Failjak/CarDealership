import django_filters
from django_filters import rest_framework as filters
from .models import Provider


class ProviderFilter(filters.FilterSet):
    start_found_year = django_filters.DateFilter(field_name='found_year', lookup_expr=('lt'))
    end_found_year = django_filters.DateFilter(field_name='found_year', lookup_expr=('gt'))

    class Meta:
        model = Provider
        fields = {
            'name': ['icontains', 'exact'],
            'cars__brand': ['icontains', 'exact'],
            'car_prices__price': ['gte', 'lte'],
        }
