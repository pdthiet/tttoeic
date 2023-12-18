from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    word = models.CharField(max_length=100)
    pos = models.CharField(max_length=50)
    pronunciation = models.CharField(max_length=100)
    meaning = models.TextField()

    def __str__(self):
        return self.word

