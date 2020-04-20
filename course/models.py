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
    isAvailable = models.BooleanField(default=False)
    price = models.FloatField(default=0)
    tutor = models.ForeignKey(User, on_delete=CASCADE, null=True)


class ShoppingCart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, to_field='id')
    number = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

