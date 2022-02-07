from django.contrib import admin

from .models import Dealer, DealerDiscount, DealerToUserOffer


@admin.register(Dealer, DealerDiscount, DealerToUserOffer)
class DealerAdmin(admin.ModelAdmin):
    pass
