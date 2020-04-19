from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    age = models.IntegerField()
    isAvailable = models.BooleanField(default=False)
    price = models.FloatField(null=True)
    phoneNumber = models.CharField(max_length=10)
    image = models.ImageField(null=True)

