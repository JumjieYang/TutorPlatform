# Generated by Django 3.0.4 on 2020-04-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderhistory', '0003_orderhistory_paymentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory',
            name='address',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
