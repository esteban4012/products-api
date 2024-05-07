from django.db import models

class Clients(models.Model):
    name = models.CharField(max_length=50)
    identification_number = models.BigIntegerField()
    adress = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name
