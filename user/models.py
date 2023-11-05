from django.db import models

# Create your models here.

companies=[
    ("1", "1"),
    ("2", "2"),
]

brands=[
    ("1", "1"),
    ("2", "2"),
]
class Register(models.Model):
    fullname = models.CharField(max_length=45,default="")
    email=models.EmailField(max_length=45,default="")
    phone = models.CharField(max_length=10,default="")
    company= models.CharField(max_length=10,choices=companies)
    brand = models.CharField(max_length=45,choices=brands)

class Experts(models.Model):
    name=models.CharField(max_length=45,default="")
    position=models.CharField(max_length=45,default="")
    img=models.FileField( upload_to='media', blank=True, null=True)
    
