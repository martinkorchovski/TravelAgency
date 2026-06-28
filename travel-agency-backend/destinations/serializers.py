from rest_framework import serializers
from .models import Destination
from hotels.serializers import HotelSerializer

class DestinationSerializer(serializers.ModelSerializer):
    hotels = HotelSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = '__all__'