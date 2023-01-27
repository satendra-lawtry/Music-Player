from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class Vender(models.Model,BaseUserManager):
    registration_no = models.CharField(max_length=50)
    spassword = models.CharField(max_length=100)
    ownername = models.CharField(max_length=100)
    shopname = models.CharField(max_length=100)
    gstno = models.CharField(max_length=100)
    shopcno = models.CharField(max_length=100)
    shopemail = models.EmailField()
    shopimage = models.ImageField(upload_to='producting')
    shopadd = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.shopname and self.ownername

CATEGORY_CHOICES =(
    ('M', 'Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW', 'Bottom Wear'),
)    
   
