from django.db import models

# Create your models here.
class Customer(models.Model):
    uname=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=15,blank=False,null=False)
    cpassword=models.CharField(max_length=15,blank=False,null=False)
    
    def __str__(self):
        return self.uname