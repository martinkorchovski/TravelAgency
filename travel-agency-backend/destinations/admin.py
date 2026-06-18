from django.contrib import admin

from destinations.models import Destination

# Register your models here.
@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'price', 'is_featured')
    list_editable = ('is_featured',)
