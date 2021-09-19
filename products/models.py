from django.db import models

# Create your models here.


class products(models.Model) :
     title = models.CharField(max_length=300)
     description = models.TextField(max_length=2000)
     image = models.ImageField(upload_to='posts/')
     colors = models.CharField(max_length=200)











class Catagories(models.Model) :
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=200)



