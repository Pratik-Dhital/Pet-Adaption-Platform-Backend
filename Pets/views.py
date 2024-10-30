from django.shortcuts import render
from rest_framework import viewsets, generics
from .serialization import *
from .models import *

# Create your views here.

class PetView(viewsets.ViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetUpdateView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer 