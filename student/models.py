from django.db import models

# Create your models here.
class Student(models.Model):
    firebase_id = models.CharField(max_length=255, unique=True)
    avatar = models.TextField(null=True)
    username = models.CharField(max_length=255)
    gender = models.BooleanField(default=True)
    phone = models.CharField(null=True, max_length=20)
    created_at = models.DateField(auto_now_add=True)
    is_vip = models.BooleanField(default=False)
    vip_start = models.DateField(null=True)
    vip_end = models.DateField(null=True)

    def __str__(self):
        return self.username


