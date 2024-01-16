from django.db import models

# Create your models here.
class Package(models.Model):
 country=models.CharField(max_length=50)
 discription=models.CharField(max_length=300,blank=True)
 image=models.CharField(max_length=300,blank=True)
 date = models.CharField(max_length=300,blank=True)
 price=models.IntegerField(default=0)
 personce=models.IntegerField(default=0)
 def _str_(self):
  return self.country
# Create your models here.