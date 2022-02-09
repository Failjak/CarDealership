from django.contrib import admin

from .models import Dealer


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    pass
