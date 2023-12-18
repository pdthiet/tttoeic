from rest_framework import serializers
from .models import *

class CreateExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = ['firebase_id', 'exam_id']

class UpdateExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = ['firebase_id', 'exam_id', 'listening_answers', 'reading_answers']

class UpdateExamScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = ['exam_id', 'firebase_id', 'listening_score', 'reading_score']
    
class GetListeningAndReadingScore(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = ['listening_score', 'reading_score']

class GetConVersionScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversionScore
        fields = ['number_of_correct_answers', 'listening', 'reading']

class GetExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = ['exam_id', 'firebase_id', 'listening_answers', 'reading_answers']

class GetLatestScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = ['exam_id', 'firebase_id', 'listening_score', 'reading_score']

class CreatePartResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartResult
        fields = ['firebase_id', 'exam_id', 'part', 'user_answers', 'grade']

class GetPartResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartResult
        fields = ['firebase_id', 'exam_id', 'part', 'user_answers', 'grade']

class GetPartResultByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartResult
        fields = '__all__'

class GetExamResultByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'
    
    