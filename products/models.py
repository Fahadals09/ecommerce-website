from django.db import models
from setting.models import Colors

# Create your models here.


class Products(models.Model) :
     title = models.CharField(max_length=100)
     description = models.TextField(max_length=2000)
     image = models.ImageField(upload_to='posts/')
     colors = models.ManyToManyField(Colors,blank=True,null=True)
     size = models.CharField(max_length=200)


     def __str__(self):
        return self.title











class Catagories(models.Model) :
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=200)



    def __str__(self):
        return self.title



