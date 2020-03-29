from django.db import models
from django.db.models import CASCADE, SET_NULL


# Create your models here.
# class OrderHistory(models.Model):
#     date = models.DateTimeField(auto_now=True)
#     amount = models.FloatField()
#     rating = models.FloatField()
#     address = models.CharField(max_length=30)
#     tutor = models.ForeignKey('Person', on_delete=SET_NULL, null=True, related_name="tutor")
#     courseList = models.ForeignKey('Course', on_delete=SET_NULL, null=True)


# class Course(models.Model):
#     subject = models.CharField(max_length=4)
#     number = models.IntegerField()
#     term = models.CharField(max_length=6)
#     description = models.CharField(max_length=100)
#     tutor = models.ForeignKey(Person,on_delete=SET_NULL,null=True)

class Person(models.Model):
    email = models.EmailField(primary_key=True, unique=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField()
    rating = models.FloatField()
    isAvailable = models.BooleanField(null=True)
    price = models.FloatField(null=True)
    phoneNumber = models.CharField(max_length=10)
    image = models.ImageField()
    # orderHistory = models.ForeignKey(OrderHistory, on_delete=CASCADE,null=True)
    # courses = models.ManyToManyField(Course,null=True,on_delete=SET_NULL)
    token = models.CharField(max_length=60)
