from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def get_audio_for_part(request):
    exam_id = request.GET['exam_id']
    part = request.GET['part']
    audioes = Audio.objects.filter(exam_id = exam_id, part = part).first()
    serializer = GetAudioSerializer(audioes)
    return Response(serializer.data)

@api_view(['GET'])
def get_audio_for_exam(request):
    exam_id = request.GET['exam_id']
    audioes = Audio.objects.filter(exam_id = exam_id, part = 0).first()
    serializer = GetAudioSerializer(audioes)
    return Response(serializer.data)

@api_view(['GET'])
def get_image(request):
    exam_id = request.GET['exam_id']
    images = Image.objects.filter(exam_id = exam_id)
    serializer = GetImageSerializer(images, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_examination(request):
    exam_id = request.GET['exam_id']
    exams = Examination.objects.filter(exam_id = exam_id).order_by('number')
    serializer = GetExaminationSerializer(exams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_examination_item(request):
    exam_id = request.GET['exam_id']
    number = request.GET['number']
    exam = Examination.objects.filter(exam_id = exam_id, number = number).first()
    serializer = GetExaminationSerializer(exam)
    return Response(serializer.data)

@api_view(['GET'])
def get_reading_examination(request):
    exam_id = request.GET['exam_id']
    exams = Examination.objects.filter(exam_id = exam_id, number__gt = 100).order_by('number')
    serializer = GetExaminationSerializer(exams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_correct_answer(request):
    exam_id = request.GET['exam_id']
    correct_answers = Examination.objects.filter(exam_id = exam_id).order_by('number')
    serializer = GetCorrectAnswerSerializer(correct_answers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_part_question(request):
    try:
        exam_id = request.GET['exam_id']
        part = request.GET['part']
    except KeyError:
        return Response({'error': 'Missing param in request.'}, status=400)

    questions = Examination.objects.filter(exam_id=exam_id, part=part).order_by('number')

    serializer = GetExaminationSerializer(questions, many=True)
    return Response(serializer.data)
