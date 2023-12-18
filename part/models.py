from django.db import models

# Create your models here.
class Part(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.TextField()
    is_vip = models.BooleanField()

    def __str__(self):
        return self.name