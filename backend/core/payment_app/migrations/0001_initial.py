# Generated by Django 5.0 on 2023-12-05 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=100, null=True)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2023, 12, 5, 18, 24, 2, 874381, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
