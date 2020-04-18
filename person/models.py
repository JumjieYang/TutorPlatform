from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    isAvailable = models.BooleanField(default=False)
    price = models.FloatField(default=0)
    phoneNumber = models.CharField(max_length=10)
    image = models.ImageField(null=True)
