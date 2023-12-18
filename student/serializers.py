from rest_framework import serializers
from .models import Student

class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['firebase_id', 'username']

class UpdateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'gender', 'phone']

class UpdateAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['avatar',]

class UpdateVipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['is_vip', 'vip_start', 'vip_end']

class GetAllStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['firebase_id', 'avatar', 'username', 'gender', 'phone','is_vip', 'vip_start', 'vip_end']
