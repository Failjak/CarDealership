from django.db import models
from djmoney.models.fields import MoneyField

from car_dealership.core import AbstractInstance


class User(AbstractInstance, models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='name')
    balance = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', verbose_name='balance')
