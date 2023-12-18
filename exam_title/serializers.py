from rest_framework import serializers
from .models import ExamTitle

class AllExamTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamTitle
        fields = ['exam_id', 'year', 'name', 'time', 'question', 'is_vip']

class CreateExamTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamTitle
        fields = ['exam_id', 'year', 'name', 'time', 'question', 'is_vip']