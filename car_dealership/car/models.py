from django.db import models
from djmoney.models.fields import MoneyField

from car_dealership.core.models import AbstractInstance


class CarConfiguration(AbstractInstance):
    engine = models.CharField(max_length=50, blank=True, verbose_name='engine')
    power = models.PositiveSmallIntegerField(verbose_name='power')
    colour = models.CharField(max_length=50, blank=True, verbose_name='colour')
    release_year = models.DateField(verbose_name='release_year')
    vehicle_cat = models.CharField(max_length=5, verbose_name='vehicle_category')
    car = models.OneToOneField(
        'car.Car',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='car_config'
    )


class Car(models.Model):
    brand = models.CharField(max_length=100, verbose_name='brand')
    model = models.CharField(max_length=100, verbose_name='model')

    def __str__(self):
        return f'{self.brand} {self.model}'


class CarPrices(AbstractInstance):
    car = models.ForeignKey('car.Car', on_delete=models.CASCADE, verbose_name='car')
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', verbose_name='price')
