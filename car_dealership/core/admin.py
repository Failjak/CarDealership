from django.contrib import admin

from .models import Offer, Discount


@admin.register(Offer, Discount)
class CoreAdmin(admin.ModelAdmin):
    pass
