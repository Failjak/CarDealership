from django.contrib import admin

from .models import Car, CarConfiguration, CarPrices


@admin.register(Car, CarConfiguration, CarPrices)
class CarAdmin(admin.ModelAdmin):
    pass
