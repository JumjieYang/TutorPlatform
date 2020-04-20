from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from course.models import ShoppingCart


# Create your models here.
class OrderHistory(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    rating = models.FloatField(null=True)
    address = models.CharField(max_length=30)
    owner = models.ForeignKey(User,on_delete= CASCADE,to_field='id')
    cart = models.ForeignKey(ShoppingCart, on_delete=CASCADE, to_field='id')
    isPayed = models.BooleanField(default=False)