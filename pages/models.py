from django.db import models

# Create your models here.
class Package(models.Model):
 country=models.CharField(max_length=50)
 discription=models.CharField(max_length=300,blank=True)
 image=models.CharField(max_length=300,blank=True)
 date = models.CharField(max_length=300,blank=True)
 price=models.IntegerField(default=0)
 personce=models.IntegerField(default=0)
 checked_out= models.CharField(max_length=10,blank=True, default='no')
 type=models.CharField(max_length=10,blank=True,default='PACKAGE')
 def _str_(self):
  return self.country
# Create your models here.
 
class Flight(models.Model):
 depart=models.CharField(max_length=50)
 destination=models.CharField(max_length=50,blank=True)
 type=models.CharField(max_length=10,blank=True,default='FLIGHT')
 classe = models.CharField(max_length=50,blank=True)
 hour_d = models.CharField(max_length=20,blank=True)
 hour_a = models.CharField(max_length=20,blank=True)
 ps1 = models.CharField(max_length=10,blank=True)
 ps2 = models.CharField(max_length=10,blank=True)
 price=models.IntegerField(default=0)
 def _str_(self):
  return self.destination