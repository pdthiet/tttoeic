from django.db import models

# Create your models here.
class Note(models.Model):
    firebase_id = models.CharField(max_length=100)
    title = models.TextField()
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
