from django.db import models

from core.models import AbstractInstance


class Provider(AbstractInstance):
    name = models.CharField(max_length=100, verbose_name='name')
    found_year = models.DateField(verbose_name='found_name')

    cars = models.ManyToManyField('car.Car', verbose_name='cars')
    car_prices = models.ManyToManyField('car.CarPrices', verbose_name='car_prices')
