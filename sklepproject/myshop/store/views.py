# views.py
from django.shortcuts import render

from .serializer import ClothingSerializer, Rates
from rest_framework import viewsets
from .models import Clothing,Rates

class ClothingViewSet(viewsets.ModelViewSet):
    queryset=Clothing.objects.all()
    serializer_class=ClothingSerializer

class RatesViewSet(viewsets.ModelViewSet):
    queryset=Rates.objects.all()
    serializer_class = Rates
