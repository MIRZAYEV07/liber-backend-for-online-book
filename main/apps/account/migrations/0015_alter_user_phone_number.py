# Generated by Django 3.2.9 on 2022-02-26 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_userbook_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(error_messages={'unique': 'User with this phone number already exists.'}, max_length=15, unique=True, verbose_name='Phone number'),
        ),
    ]
