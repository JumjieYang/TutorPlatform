from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    age = models.IntegerField()
    phoneNumber = models.CharField(max_length=10)
    isTutor = models.BooleanField(default=False)
    image = models.CharField(max_length=1000000, null=True)

