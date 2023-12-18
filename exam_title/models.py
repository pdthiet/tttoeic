from django.db import models

# Create your models here.
class ExamTitle(models.Model):
    exam_id = models.CharField(max_length=50)
    year = models.IntegerField()
    name = models.CharField(max_length=50)
    time = models.IntegerField()
    question = models.IntegerField()
    is_vip = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)