from django.db import models

# Create your models here.
class Post(models.Model):
    name= models.CharField(max_length=20)
    mail= models.CharField(max_length=50)
    number= models.CharField(max_length=11)
    textarea= models.CharField(max_length=2000)
