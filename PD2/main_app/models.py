from django.db import models

# Create your models here.

class Load(models.Model):
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    rate = models.CharField(default="", editable=True, max_length=255)
    total_km = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


def __str__(self):
    return self.name
