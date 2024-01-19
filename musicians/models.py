from django.db import models

# Create your models here.

class MusicianModel(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField( max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField()
    instrument_type = models.CharField(max_length=100)
