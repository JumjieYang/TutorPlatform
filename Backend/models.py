from django.db import models
from django.db.models import CASCADE, SET_NULL

# Create your models here.
class OrderHistory(models.Model):
    date = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    rating = models.FloatField()
    address = models.CharField(max_length=30)
    tutor = models.ForeignKey('Person',on_delete=SET_NULL,null=True,related_name="tutor")
    tutee = models.ForeignKey('Person',on_delete=SET_NULL,null=True)
    courseList = models.ForeignKey('Course',on_delete=SET_NULL,null=True)

class Person(models.Model):
    email = models.EmailField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField()
    Subject = models.TextField(null=True)
    rating = models.FloatField()
    isAvailable = models.BooleanField()
    price = models.FloatField()
    phoneNumber = models.CharField(max_length=10)
    orderHistory = models.ForeignKey(OrderHistory,on_delete=CASCADE)
    
    @property
    def getName(self):
        return self.firstName +' '+self.lastName
class Course(models.Model):
    subject = models.CharField(max_length=4)
    number = models.IntegerField()
    term = models.CharField(max_length=6)
    description = models.CharField(max_length=100)

    @property
    def getCourse(self):
        return self.Subject+self.Number

