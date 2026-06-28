from django.contrib import admin
from .models import Hotel


# Register your models here.
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'stars', 'rating', 'price_per_night')
    list_filter = ('stars', 'destination')