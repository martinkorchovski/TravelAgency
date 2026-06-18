from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Booking
from .serializers import BookingSerializer


# Create your views here.

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        destination = serializer.validated_data['destination']
        persons = serializer.validated_data['persons']
        total_price = destination.price * persons
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user, total_price=total_price)
        else:
            serializer.save(total_price=total_price)


class BookingDetailView(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_booking_status(request, pk):
    try:
        booking = Booking.objects.get(id=pk)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=404)
    new_status = request.data.get('status')
    if new_status not in ['pending', 'confirmed', 'cancelled']:
        return Response({'error': 'Invalid status'}, status=400)
    booking.status = new_status
    booking.save()
    return Response(BookingSerializer(booking).data)