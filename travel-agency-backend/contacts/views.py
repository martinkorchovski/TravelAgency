from django.shortcuts import render
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer


# Create your views here.

class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
