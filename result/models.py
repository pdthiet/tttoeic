from django.db import models

# Create your models here.
class ExamResult(models.Model):
    firebase_id = models.CharField(max_length=50)
    exam_id = models.CharField(max_length=50)
    listening_answers = models.TextField(null=True)
    reading_answers = models.TextField(null=True)
    listening_score = models.IntegerField(null=True)
    reading_score = models.IntegerField(null=True)
    updated_at = models.DateTimeField(auto_now=True)

class PartResult(models.Model):
    firebase_id = models.CharField(max_length=50)
    exam_id = models.CharField(max_length=50)
    part = models.IntegerField()
    user_answers = models.TextField(null=True)
    grade = models.CharField(max_length=20,null=True)
    updated_at = models.DateTimeField(auto_now=True)

class ConversionScore(models.Model):
    number_of_correct_answers = models.IntegerField()
    listening = models.IntegerField()
    reading = models.IntegerField()

