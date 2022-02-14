from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Discount, Offer
from .serializer import OfferSerializer, DiscountSerializer
from .filters import OfferFilter, DiscountFilter


class OfferViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    serializer_class = OfferSerializer
    queryset = Offer.objects.all()

    filter_class = OfferFilter
    ordering_fields = ['car__brand', 'provider__name', 'dealer__name', 'max_price']


class DiscountViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()

    filter_class = DiscountFilter
    ordering_fields = ['car__brand', 'provider__name', 'dealer__name', 'percent']
