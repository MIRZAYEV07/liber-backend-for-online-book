# Generated by Django 3.2.9 on 2022-03-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_auto_20220311_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_canceled',
            field=models.BooleanField(default=False),
        ),
    ]
