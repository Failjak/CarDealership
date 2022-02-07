from django.contrib import admin

from .models import Provider, ProviderDiscount, ProviderToDealerOffer


@admin.register(Provider, ProviderDiscount, ProviderToDealerOffer)
class ProviderAdmin(admin.ModelAdmin):
    pass
