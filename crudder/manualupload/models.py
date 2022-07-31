from django.db import models

# Create your models here.


class Student(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    rollno = models.IntegerField()
    grade = models.IntegerField()
    division = models.CharField(max_length=1)
    mobno = models.CharField(max_length=12)
