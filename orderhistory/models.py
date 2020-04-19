from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from course.models import Course


# Create your models here.
class OrderHistory(models.Model):
    date = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    rating = models.FloatField(null=True)
    address = models.CharField(max_length=30)
    owner = models.ForeignKey(User,on_delete= CASCADE, null=True)
    courseList = models.ForeignKey(Course, on_delete=CASCADE, null=True)
    isPayed = models.BooleanField(default=False)
