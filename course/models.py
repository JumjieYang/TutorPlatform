from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


# Create your models here.


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=4)
    number = models.IntegerField()
    term = models.CharField(max_length=6)
    time_chosed = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    tutor = models.ForeignKey(User, on_delete=CASCADE, null=True)


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    courseList = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
