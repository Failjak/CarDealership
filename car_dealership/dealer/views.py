from rest_framework import mixins
from rest_framework import viewsets

from .models import Dealer
from .serializer import DealerSerializer, DealerCreateSerializer
from .filters import DealerFilter


class DealerViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Dealer.objects.all()

    def get_serializer_class(self):
        if self.action == 'update':
            return DealerSerializer
        else:
            return DealerCreateSerializer

    filter_class = DealerFilter
    ordering_fields = ['name', 'balance', 'cars__brand', 'users__user__name']
