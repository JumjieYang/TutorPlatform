from django.db import models

# Create your models here.
class OrderHistory(models.Model):
    date = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    rating = models.FloatField()
    address = models.CharField(max_length=30)
    tutor = models.ForeignKey('Person', on_delete=SET_NULL, null=True, related_name="tutor")
    courseList = models.ForeignKey('Course', on_delete=SET_NULL, null=True)
