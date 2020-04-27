from django.db import models


# Create your models here.
class WaterMark(models.Model): 
    #name = models.CharField(max_length=50) 
    coverImg = models.ImageField(upload_to='input/')
    watermarkImg = models.ImageField(upload_to='input/')

