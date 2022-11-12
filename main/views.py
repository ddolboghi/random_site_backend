from django.shortcuts import render
from .models import Alldata, Result
from rest_framework import generics
from .serializers import AlldataSerializer, ResultSerializer

class DetailAlldata(generics.RetrieveUpdateDestroyAPIView):
  queryset = Alldata.objects.all()
  serializer_class = AlldataSerializer

class DetailResult(generics.RetrieveUpdateDestroyAPIView):
  queryset = Result.objects.all()
  serializer_class = ResultSerializer
  
  