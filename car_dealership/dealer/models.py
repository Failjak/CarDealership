from django.db import models
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField

from core.models import AbstractInstance


class Dealer(AbstractInstance):
    name = models.CharField(max_length=150, verbose_name='name')
    location = CountryField(verbose_name='location')

    balance = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', verbose_name='balance')

    cars = models.ManyToManyField('car.Car',
                                  null=True,
                                  blank=True,
                                  related_name='cars',
                                  verbose_name='cars')
    car_prices = models.ManyToManyField('car.CarPrices',
                                        null=True,
                                        blank=True,
                                        verbose_name='car_prices',
                                        related_name='car_prices',
                                        )
    cars_config = models.ManyToManyField('car.CarConfiguration',
                                         null=True, blank=True,
                                         related_name='cars_config',
                                         verbose_name='cars_config'
                                         )
    users = models.ManyToManyField('customer.Customer',
                                   null=True,
                                   blank=True,
                                   related_name='customer',
                                   verbose_name='customer')
