from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import Contact

# Create your views here.

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.ojects.all()
    serializer_class = ContactSerializer

