from rest_framework import serializers

from .models import Dealer


class DealerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'
        read_only_fields = ('balance', )
