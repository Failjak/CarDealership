from rest_framework import mixins
from rest_framework import viewsets

from .models import Discount, Offer
from .serializer import OfferSerializer, DiscountSerializer


class OfferViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class DiscountViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
