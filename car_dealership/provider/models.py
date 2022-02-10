from django.db import models

from car_dealership.core import Offer, AbstractInstance, Discount


class Provider(AbstractInstance, models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    found_year = models.DateField(verbose_name='found_name')

    cars = models.ManyToManyField('car.Car', verbose_name='cars')
    car_prices = models.ManyToManyField('car.CarPrices', verbose_name='car_prices')


class ProviderToDealerOffer(AbstractInstance, Offer, models.Model):
    dealer = models.ForeignKey('dealer.Dealer', on_delete=models.CASCADE, verbose_name='dealer')
    provider = models.ForeignKey('provider.Provider', on_delete=models.CASCADE, verbose_name='provider')


class ProviderDiscount(Discount, models.Model):
    provider = models.ForeignKey('provider.Provider', on_delete=models.CASCADE, verbose_name='provider')
