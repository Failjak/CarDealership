import django_filters
from django_filters import rest_framework as filters
from .models import Offer, Discount


class OfferFilter(filters.FilterSet):
    start_sell_date = django_filters.DateFilter(field_name='sell_date', lookup_expr=('lt'))
    end_sell_date = django_filters.DateFilter(field_name='sell_date', lookup_expr=('gt'))

    class Meta:
        model = Offer
        fields = {
            'car__brand': ['icontains', 'exact'],
            'car__model': ['icontains', 'exact'],
            'provider__name': ['icontains', 'exact'],
            'dealer__name': ['icontains', 'exact'],
            'customer__name': ['icontains', 'exact'],
            'max_price': ['gte', 'lte'],
        }


class DiscountFilter(filters.FilterSet):
    time_start = filters.RangeFilter()
    time_end = filters.RangeFilter()

    class Meta:
        models = Discount
        fields = {
            'percent': ['gte', 'lte'],
            'provider__name': ['icontains', 'exact'],
            'dealer__name': ['icontains', 'exact'],
        }
