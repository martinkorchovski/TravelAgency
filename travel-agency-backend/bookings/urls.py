from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookingListCreateView.as_view()),
    path('<int:pk>/', views.BookingDetailView.as_view()),
    path('my/',views.my_bookings),
    path('<int:pk>/status/',views.update_booking_status),
]