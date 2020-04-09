from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .models import housingsociety
from .models import blocks
from .models import apartment
from .models import citizens

from .serializers import blockserializer
from .serializers import housingserializer
from .serializers import apartmentserializer
from .serializers import citizensserializer

# Create your views here.
class housingsocietyList(APIView):
    def get(self, request):
        housing1 = housingsociety.objects.all()
        serializer = housingserializer(housing1, many=True)
        return Response(serializer.data)
    def post(self):
        pass

class blockList(APIView):
    def get(self, request):
        blocks1 = blocks.objects.all()
        serializer = blockserializer(blocks1, many=True)
        return Response(serializer.data)
    def post(self):
        pass

class apartmentList(APIView):
    def get(self, request):
        apartment1=apartment.objects.all()
        serializer=apartmentserializer(apartment1, many=True)
        return Response(serializer.data)
    def post(self):
        pass

class citizensList(APIView):
    def get(self, request):
        citizens1=citizens.objects.all()
        serializer=citizensserializer(citizens1, many=True)
        return Response(serializer.data)
    def post(self):
        pass

