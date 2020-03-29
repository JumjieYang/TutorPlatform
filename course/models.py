from django.db import models

# Create your models here.

class Course(models.Model):
    subject = models.CharField(max_length=4)
    number = models.IntegerField()
    term = models.CharField(max_length=6)
    description = models.CharField(max_length=100)
    tutor = models.ForeignKey(Person,on_delete=SET_NULL,null=True)