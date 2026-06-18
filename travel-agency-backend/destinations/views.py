from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Destination
from .serializers import DestinationSerializer

# Create your views here.

@api_view(['GET'])
def destination_list(request):
    destinations = Destination.objects.all()

    # filter po zemja
    country = request.query_params.get('country')
    if country:
        destinations = destinations.filter(country__icontains=country)

    # filter po grad
    city = request.query_params.get('city')
    if city:
        destinations = destinations.filter(city__icontains=city)

    # filter po max cena
    max_price = request.query_params.get('max_price')
    if max_price:
        destinations = destinations.filter(price__lte=max_price)

    # filter po min cena
    min_price = request.query_params.get('min_price')
    if min_price:
        destinations = destinations.filter(price__gte=min_price)

    # filter po min rating
    min_rating = request.query_params.get('min_rating')
    if min_rating:
        destinations = destinations.filter(rating__gte=min_rating)

    # prebaruvanje po ime
    search = request.query_params.get('search')
    if search:
        destinations = destinations.filter(name__icontains=search)

    # sortiranje
    ordering = request.query_params.get('ordering', 'price')
    if ordering in ['price', '-price', 'rating', '-rating', 'name', '-name']:
        destinations = destinations.order_by(ordering)

    serializer = DestinationSerializer(destinations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def destination_details(request, pk):
    try:
        destination = Destination.objects.get(id=pk)
    except Destination.DoesNotExist:
        return Response({'error': 'Destination not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = DestinationSerializer(destination)
    return Response(serializer.data)