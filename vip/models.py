from django.db import models

# Create your models here.
class VipPrice(models.Model):
    month = models.IntegerField()
    price = models.IntegerField()
    sale_price = models.IntegerField()

class VipFunction(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.TextField(null=True)

    def __str__(self):
        return self.name