# Generated by Django 3.2.9 on 2022-03-23 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_user_unique_identifier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_deleted',
        ),
    ]
