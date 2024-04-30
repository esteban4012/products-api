from django.db import models

class Product(models.Model):
    name = models.CharField(maxlength=50)
    description = models.CharField(maxlength=50)
    price = models.IntegerField()
    enable = models.BooleanField(default = True)
    
