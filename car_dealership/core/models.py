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
    max_price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', verbose_name='max_price')
    car = models.ForeignKey('car.Car', on_delete=models.CASCADE, verbose_name='car_to_offer')
    sell_date = models.DateField(auto_now_add=True, verbose_name='sell_date')

    provider = models.ForeignKey(
        'provider.Provider',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='provider_offer',
    )
    dealer = models.ForeignKey(
        'dealer.Dealer',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='dealer_offer',
    )
    customer = models.ForeignKey(
        'customer.Customer',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='customer_offer'
    )


class Discount(AbstractInstance):
    time_start = models.DateField(auto_now_add=datetime.now().time(), verbose_name='time_start')
    time_end = models.DateField(auto_now_add=datetime.now().time(), verbose_name='time_end')
    discount_cars = models.ManyToManyField('car.Car', verbose_name='discount_cars')
    percent = models.PositiveSmallIntegerField(verbose_name='stock_percentage')
    description = models.TextField(max_length=500, verbose_name='description')

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
