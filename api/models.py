from django.db import models
from django.db.models.base import Model

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=30)
    Age=models.IntegerField(default=20)
    FatherName=models.CharField(max_length=30)
