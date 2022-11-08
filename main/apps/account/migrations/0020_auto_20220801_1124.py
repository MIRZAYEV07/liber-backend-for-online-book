# Generated by Django 3.2.9 on 2022-08-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_auto_20220323_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_virified',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
