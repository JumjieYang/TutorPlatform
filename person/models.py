from django.contrib.auth.models import User
from django.db import models


def custom_upload_path(instance, filename):
    class_name = instance.__class__.__name__.lower()
    return "{}/{}-{}/{}".format(class_name + "s", class_name, instance.pk, filename)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    age = models.IntegerField()
    phoneNumber = models.CharField(max_length=10)
    isTutor = models.BooleanField(default=False)
    image = models.ImageField(upload_to=custom_upload_path, null=True)

