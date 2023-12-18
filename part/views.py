from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Part
from .serializers import *
# Create your views here.
@api_view(['GET'])
def all_part(request):
    parts = Part.objects.all()
    serializer = AllPartSerializer(parts, many=True)
    return Response(serializer.data)