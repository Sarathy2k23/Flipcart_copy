from django.db import models

class Users(models.Model):
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=50)
class Person(models.Model):
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)    