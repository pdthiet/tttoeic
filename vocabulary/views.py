from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vocabulary
from .serializers import *
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def get_all_vocabulary(request):
    vocabs = Vocabulary.objects.all()
    serializer = GetAllVocabularySerializer(vocabs, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def create_vocabulary(request):
    if request.method == 'POST':
        serializer = CreateVocabularySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_vocabulary(request):
    word = request.GET['word']
    try:
        vocabulary = Vocabulary.objects.get(word=word)
    except Vocabulary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UpdateVocabularySerializer(vocabulary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_vocabulary(request):
    word = request.GET['word']
    try:
        vocabulary = Vocabulary.objects.get(word=word)
    except Vocabulary.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        vocabulary.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
