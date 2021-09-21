from django.db import models
from colorfield.fields import ColorField

# Create your models here.


class Colors(models.Model) :
    name= models.CharField(max_length=200)
    color = ColorField(default='#FF0000')



    def __str__(self):
        return self.name

#class Size(models.Model) :
    #name= models.CharField(max_length=100)
     #size = FileSizeField(default='s')


class Company(models.Model) :
    name=models.CharField(max_length=200)
    logo=models.CharField(max_length=200)



class About(models.Model) :
    image = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=220)
    description = models.TextField(max_length=9000)


