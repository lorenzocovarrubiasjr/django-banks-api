from django.db import models

# Create your models here

class Branch(models.Model):
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  zipcode = models.PositiveIntegerField()

class Employee(models.Model):
  branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  position = models.CharField(max_length=50)
  start_date = models.DateTimeField(auto_now_add=True)
  
