from django_filters import rest_framework as filters
from .models import Dealer


class DealerFilter(filters.FilterSet):
    class Meta:
        model = Dealer
        fields = {
            'name': ['icontains', 'exact'],
            'location': ['exact'],
            'balance': ['gte', 'lte'],
            'users__name': ['icontains', 'exact'],
        }
