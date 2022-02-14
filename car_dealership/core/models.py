from django.db import models
from datetime import datetime
from djmoney.models.fields import MoneyField


class AbstractInstance(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='is_active')
    change_date = models.DateField(auto_now=True, verbose_name='change_date')
    create_date = models.DateField(auto_now_add=True, verbose_name='create_date')

    class Meta:
        abstract = True


class Offer(models.Model):
    max_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', verbose_name='MaxOfferPrice')
    car = models.ForeignKey('car.Car', on_delete=models.CASCADE, verbose_name='OfferCar')
    sell_date = models.DateField(auto_now_add=True, verbose_name='OfferSellDate')

    provider = models.ForeignKey(
        'provider.Provider',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='OfferProvider',
    )
    dealer = models.ForeignKey(
        'dealer.Dealer',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='OfferDealer',
    )
    customer = models.ForeignKey(
        'customer.Customer',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='OfferCustomer'
    )


class Discount(AbstractInstance):
    time_start = models.DateField(auto_now_add=datetime.now().time(), verbose_name='DiscountStartTime')
    time_end = models.DateField(auto_now_add=datetime.now().time(), verbose_name='DiscountTimeEnd')
    discount_cars = models.ManyToManyField('car.Car', verbose_name='discount_cars')
    percent = models.PositiveSmallIntegerField(verbose_name='DiscountPercent')
    description = models.TextField(max_length=500)

    provider = models.ForeignKey(
        'provider.Provider',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='provider_discount',
    )
    dealer = models.ForeignKey(
        'dealer.Dealer',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='dealer_discount',
    )
