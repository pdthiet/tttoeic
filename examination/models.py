from django.db import models

# Create your models here.
class Audio(models.Model):
    exam_id = models.CharField(max_length=50)
    part = models.IntegerField()
    audio_url = models.TextField()

    def __str__(self):
        return f"{self.exam_id}, {self.part}"
    
class Image(models.Model):
    exam_id = models.CharField(max_length=50)
    number = models.IntegerField()
    image_url = models.TextField()

    def __str__(self):
        return f"{self.exam_id}, {self.number}"
    
class Examination(models.Model):
    exam_id = models.CharField(max_length=50)
    part = models.IntegerField()
    number = models.IntegerField()
    image_url = models.TextField(null=True)
    paragraph = models.TextField(null = True)
    question = models.TextField(null = True)
    option1 = models.TextField(null = True)
    option2 = models.TextField(null = True)
    option3 = models.TextField(null = True)
    option4 = models.TextField(null = True)
    correct_answer = models.CharField(max_length=5)
    explaination = models.TextField(null=True)