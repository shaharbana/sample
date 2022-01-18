from django.db import models

# Create your models here.
class user_tb(models.Model):
    name=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    username=models.CharField(max_length=20,default="none")
    password=models.CharField(max_length=20,default="none")
    status=models.CharField(max_length=20,default="pending")
class admin_tb(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class rating_tb(models.Model):
    rate=models.FloatField()
    feedback=models.CharField(max_length=50)
   
