from rest_framework import serializers
from .models import Note

class CreateNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['firebase_id', 'title', 'content']

class GetNoteByFireBaseIdSerializer (serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'firebase_id', 'title', 'content']

class UpdateNoteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'content']