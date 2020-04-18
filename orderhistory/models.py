from django.db import models
from django.db.models import SET_NULL
from course.models import Course


# Create your models here.
class OrderHistory(models.Model):
    date = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    rating = models.FloatField()
    address = models.CharField(max_length=30)
    courseList = models.ForeignKey(Course, on_delete=SET_NULL, null=True)
