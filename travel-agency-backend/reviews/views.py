from django.shortcuts import render
from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer

# Create your views here.
class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()
        hotel_id = self.request.query_params.get('hotel')
        if hotel_id:
            queryset = queryset.filter(hotel_id=hotel_id)
        return queryset.order_by('-created_at')