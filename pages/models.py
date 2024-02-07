from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Package(models.Model):
 id = models.AutoField(primary_key=True)
 country=models.CharField(max_length=100)
 discription=models.CharField(max_length=500,blank=True)
 date = models.CharField(max_length=300,blank=True)
 price=models.IntegerField(default=0)
 personce=models.IntegerField(default=0)
 checked_out_by = models.ManyToManyField(User, blank=True)  # ManyToManyField with User
 type=models.CharField(max_length=10,blank=True,default='PACKAGE')
 pack_image = models.ImageField(null=True, blank=True, upload_to="images/")

 def _str_(self):
  return self.country
# Create your models here.
 
class Flight(models.Model): 
 id = models.AutoField(primary_key=True)
 depart=models.CharField(max_length=50)
 destination=models.CharField(max_length=50,blank=True)
 type=models.CharField(max_length=10,blank=True,default='FLIGHT')
 image=models.CharField(max_length=300,blank=True)
 classe = models.CharField(max_length=50,blank=True)
 hour_d = models.CharField(max_length=20,blank=True)
 hour_a = models.CharField(max_length=20,blank=True)
 ps1 = models.CharField(max_length=10,blank=True)
 ps2 = models.CharField(max_length=10,blank=True)
 price=models.IntegerField(default=0)
 checked_out_by = models.ManyToManyField(User, blank=True)  # ManyToManyField with User

 def _str_(self):
  return self.destination
 

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    last_name = models.CharField(max_length=255,blank=True)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    type = models.CharField(max_length=255,blank=True)

 
    def _str_(self):
     return self.recipient
 