from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from django.shortcuts import get_object_or_404 
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

@api_view(['POST'])
def create_student(request):
    if request.method == 'POST':
        serializer = CreateStudentSerializer(data=request.data)
        if serializer.is_valid():
            firebase_id = request.data.get('firebase_id')
            try:
                student = Student.objects.get(firebase_id=firebase_id)
                return Response({"existed":True}, status=401) 
            except:
                serializer.save()
                return Response({"isSuccess":True, "message":"Create student successfully!"}, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET'])
def check_new_firebase_id(request):
    firebase_id = request.GET.get('firebase_id')
    student = Student.objects.filter(firebase_id=firebase_id).first()
    if student is None:
        return Response({"message":"This firebase id does not exist in db"}, status=200)
    return Response({"message":"This firebase id existed"}, status=400)

@api_view(['GET'])
def get_student_by_id(request):
    firebase_id = request.GET.get('firebase_id')
    student = get_object_or_404(Student, firebase_id=firebase_id)
    student_data = {
        'avatar' : student.avatar,
        'username' : student.username,
        'gender' : student.gender,
        'phone' : student.phone,
        'is_vip' : student.is_vip,
        'vip_start' : student.vip_start,
        'vip_end' : student.vip_end
    }
    return Response(student_data, status=200)

@api_view(['PUT'])
def update_student(request, firebase_id):
    try:
        student = Student.objects.get(firebase_id=firebase_id)
    except Student.DoesNotExist:
        return Response({"error": "Student not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = UpdateStudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_avatar(request, firebase_id):
    try:
        student = Student.objects.get(firebase_id=firebase_id)
    except Student.DoesNotExist:
        return Response({"error": "Student not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = UpdateAvatarSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_vip(request):
    firebase_id = request.GET['firebase_id']
    month = int(request.GET['month'])
    try:
        student = Student.objects.get(firebase_id = firebase_id)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    
    current_date = timezone.now().date()
    
    if not student.is_vip:
        if student.vip_start is None:
            student.vip_start = current_date
        
        student.vip_end = student.vip_start + timedelta(days = month * 30)
        student.is_vip = True
        student.save()
        return Response({'message': 'VIP status updated'}, status=status.HTTP_200_OK)
    
    return Response({'message': 'VIP status unchanged'}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def check_vip_and_update(request):
    firebase_id = request.GET['firebase_id']
    try:
        student = Student.objects.get(firebase_id = firebase_id)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Kiểm tra và cập nhật trạng thái VIP
    current_date = timezone.now().date()
    if student.is_vip and current_date >= student.vip_end:
        student.is_vip = False
        student.save()
        return Response({'message': 'VIP status updated'}, status=status.HTTP_200_OK)
    return Response({'message': 'VIP status not updated'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([])
def check_superuser(request):
    if request.method == "POST":
        username = request.GET['username']
        password = request.GET['password']

        # Xác thực người dùng
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                return Response({"message": "User is a superuser."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "User is not a superuser."}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "User not found or authentication failed."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_student(request):
    students = Student.objects.all()
    serializer = GetAllStudentSerializer(students, many = True)
    return Response(serializer.data)