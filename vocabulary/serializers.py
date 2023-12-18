from rest_framework import serializers
from .models import Vocabulary

class GetAllVocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ['word', 'pos', 'pronunciation', 'meaning']

class CreateVocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ['word', 'pos', 'pronunciation', 'meaning']

class UpdateVocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ['word', 'pos', 'pronunciation', 'meaning']
    