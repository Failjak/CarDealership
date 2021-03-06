from rest_framework import mixins
from rest_framework import viewsets

from .models import Customer
from .serializer import CustomerCreateSerializer, CustomerSerializer


class CustomerViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return CustomerSerializer
        else:
            return CustomerCreateSerializer
