# Generated by Django 5.0 on 2023-12-05 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 23, 54, 34, 151112)),
        ),
    ]