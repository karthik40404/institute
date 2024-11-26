from django.db import models

# Create your models here.
class Course(models.Model):
    cid=models.TextField()
    cname=models.TextField()
    disc=models.TextField()
    price=models.IntegerField()
    img=models.FileField()

class Message(models.Model):
    name=models.TextField()
    email=models.EmailField()
    message=models.TextField()