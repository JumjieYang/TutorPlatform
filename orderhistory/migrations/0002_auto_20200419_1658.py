# Generated by Django 3.0.4 on 2020-04-19 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0003_shoppingcart'),
        ('orderhistory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory',
            name='isPayed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='courseList',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
