from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from animal1.models import Animal
from animal1.serializer import AnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

#class AnimalAPIView(generics.ListAPIView):
    #queryset = Animal.objects.all()
    #serializer_class = AnimalSerializer


#class AnimalAPIViewUpdate(generics.UpdateAPIView):
    #queryset = Animal.objects.all()
    #serializer_class = AnimalSerializer


#class AnimalAPIViewDetail(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Animal.objects.all()
    #serializer_class = AnimalSerializer
