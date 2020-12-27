from django.db import models

# Create your models here.
class medii(models.Model):

    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=100)
    rs=models.IntegerField()
class medo(models.Model):
    img=models.ImageField(upload_to='pi')
