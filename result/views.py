from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.db.models import Max

@api_view(['POST'])
def create_exam_result(request):
    if request.method == 'POST':
        serializer = CreateExamResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_exam_result(request):
    try:
        exam_id = request.GET['exam_id']
        firebase_id = request.GET['firebase_id']
        exam_result = ExamResult.objects.filter(exam_id = exam_id, firebase_id = firebase_id).latest('updated_at')
    except ExamResult.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UpdateExamResultSerializer(exam_result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_exam_score(request):
    try:
        exam_id = request.GET['exam_id']
        firebase_id = request.GET['firebase_id']
        exam_result = ExamResult.objects.filter(exam_id = exam_id, firebase_id = firebase_id).latest('updated_at')
    except ExamResult.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UpdateExamScoreSerializer(exam_result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_listening_and_reading_score(request):
    firebase_id = request.GET['firebase_id']
    exam_id = request.GET['exam_id']
    score = ExamResult.objects.filter(firebase_id = firebase_id, exam_id = exam_id).latest('updated_at')
    serializer = GetListeningAndReadingScore(score)
    return Response(serializer.data)

@api_view(['GET'])
def get_conversion_score(request):
    number_of_correct_answers = request.GET['number_of_correct_answers']
    scores = ConversionScore.objects.get(number_of_correct_answers = number_of_correct_answers)
    serializer = GetConVersionScoreSerializer(scores)
    return Response(serializer.data)

@api_view(['GET'])
def get_student_answer(request):
    exam_id = request.GET['exam_id']
    firebase_id = request.GET['firebase_id']
    answer = ExamResult.objects.filter(exam_id = exam_id, firebase_id = firebase_id).latest('updated_at')
    serializer = GetExamResultSerializer(answer)
    return Response(serializer.data)

@api_view(['GET'])
def get_latest_score(request):
    try:
        firebase_id = request.GET['firebase_id']
    except KeyError:
        return Response({'error': 'Missing firebase_id in request.'}, status=400)

    latest_scores = ExamResult.objects.filter(firebase_id=firebase_id) \
        .values('exam_id') \
        .annotate(max_updated_at=Max('updated_at')) \
        .order_by('exam_id')
    
    scores_list = []

    for score in latest_scores:
        latest_score = ExamResult.objects.filter(firebase_id=firebase_id, exam_id=score['exam_id'], updated_at=score['max_updated_at']).first()
        if latest_score:
            scores_list.append(latest_score)

    # Sử dụng serializer để chuyển đổi danh sách điểm thành dạng JSON
    serializer = GetLatestScoreSerializer(scores_list, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def create_part_result(request):
    if request.method == 'POST':
        serializer = CreatePartResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the student's score to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_part_result(request):
    try:
        firebase_id = request.GET['firebase_id']
        exam_id = request.GET['exam_id']
        part = request.GET['part']
    except KeyError:
        return Response({'error': 'Missing in request.'}, status=400)

    latest_scores = PartResult.objects.filter(firebase_id=firebase_id, exam_id = exam_id, part = part).latest('updated_at')
    
    serializer = GetPartResultSerializer(latest_scores)

    return Response(serializer.data)

@api_view(['GET'])
def get_part_result_by_user(request):
    try:
        firebase_id = request.GET['firebase_id']
    except KeyError:
        return Response({'error': 'Missing in request.'}, status=400)

    results = PartResult.objects.filter(firebase_id=firebase_id).order_by('-updated_at')
    
    serializer = GetPartResultByUserSerializer(results, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def get_exam_result_by_user(request):
    try:
        firebase_id = request.GET['firebase_id']
    except KeyError:
        return Response({'error': 'Missing in request.'}, status=400)

    results = ExamResult.objects.filter(firebase_id=firebase_id).order_by('-updated_at')
    
    serializer = GetExamResultByUserSerializer(results, many = True)

    return Response(serializer.data)
