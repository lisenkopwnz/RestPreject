from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from animal1.models import Animal
from animal1.serializer import WomenSerializer


#class WomenAPIView(generics.ListAPIView):
#queryset = Women.objects.all()
#serializer_class = WomenSerializer

class AnimalAPIView(APIView):

    def get(self, request):
        return Response({'title': 'xuy'})
