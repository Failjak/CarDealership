from rest_framework import serializers

from .models import Car, CarPrices, CarConfiguration


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarPricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPrices
        fields = '__all__'


class CarConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarConfiguration
        fields = '__all__'
