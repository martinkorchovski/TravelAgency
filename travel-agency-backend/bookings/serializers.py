from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    destination_name = serializers.CharField(source='destination.name', read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['status', 'total_price', 'created_at']