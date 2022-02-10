from rest_framework import mixins
from rest_framework import viewsets

from .models import Provider
from .serializers import ProviderSerializer


class ProviderViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
