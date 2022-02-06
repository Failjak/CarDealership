from django.db import models
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField

from core.models import AbstractInstance, Discount, Offer


class Dealer(AbstractInstance, models.Model):
    name = models.CharField(max_length=150, verbose_name='name')
    location = CountryField(verbose_name='location')

    balance = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', verbose_name='balance')

    cars = models.ManyToManyField('car.Car', related_name='cars', verbose_name='cars')
    car_prices = models.ManyToManyField('car.CarPrices', verbose_name='car_prices')
    cars_config = models.ManyToManyField('car.CarConfiguration', related_name='cars_config', verbose_name='cars_config')
    users = models.ManyToManyField('user.User', verbose_name='users')


class DealerToUserOffer(AbstractInstance, Offer, models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='user')
    dealer = models.ForeignKey('dealer.Dealer', on_delete=models.CASCADE, verbose_name='dealer')


class DealerDiscount(Discount, models.Model):
    dealer = models.ForeignKey('dealer.Dealer', on_delete=models.CASCADE)
