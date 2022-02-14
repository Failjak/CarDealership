from django_filters import rest_framework as filters
from .models import Customer


class CustomerFilter(filters.FilterSet):
    class Meta:
        model = Customer
        fields = {
            'name': ['icontains', 'exact'],
            'balance': ['gte', 'lte'],
        }