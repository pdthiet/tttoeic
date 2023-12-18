from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ExamTitle
from .serializers import *
# Create your views here.
@api_view(['GET'])
def all_exam_title(request):
    parts = ExamTitle.objects.all().order_by('name')
    serializer = AllExamTitleSerializer(parts, many=True)
    return Response(serializer.data)

# Create your views here.
@api_view(['GET'])
def get_exam_title(request, exam_id):
    exam = ExamTitle.objects.filter(exam_id = exam_id).first()
    serializer = AllExamTitleSerializer(exam)
    return Response(serializer.data)

@api_view(['POST'])
def create_exam_info(request):
    exam_id = request.data.get('exam_id')
    
    # Kiểm tra xem exam_id đã tồn tại
    if ExamTitle.objects.filter(exam_id=exam_id).exists():
        return Response({'error': 'exam_id existed'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = CreateExamTitleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_exam_info(request):
    exam_id = request.GET["exam_id"]
    try:
        exam = ExamTitle.objects.get(exam_id=exam_id)
    except ExamTitle.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CreateExamTitleSerializer(exam, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_exam_info(request):
    exam_id = request.GET['exam_id']
    try:
        exam = ExamTitle.objects.get(exam_id=exam_id)
    except ExamTitle.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    exam.delete()
    return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)