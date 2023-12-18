from rest_framework import serializers
from .models import *

class GetAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['exam_id', 'part', 'audio_url']
    
class GetImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['exam_id', 'number', 'image_url']

class GetExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = '__all__'
    
class GetCorrectAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = ['number', 'correct_answer']