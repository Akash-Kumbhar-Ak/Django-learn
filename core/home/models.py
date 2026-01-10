from django.db import models

# Create your models here.
class Student(models.Model):
    # id=models.AutoField(primary_key=True) add the django automatically
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    image=models.ImageField()
    city=models.CharField(max_length=100)

class Product(models.Model):
    pass