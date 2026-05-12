from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Destination
from .serializers import DestinationSerializer

# Create your views here.

@api_view(['GET'])
def destination_list(request):
    destinations = Destination.objects.all()
    serializer = DestinationSerializer(destinations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def destination_details(request, pk):
    destination = Destination.objects.get(id=pk)
    serializer = DestinationSerializer(destination)
    return Response(serializer.data)