# Generated by Django 3.2.9 on 2022-03-23 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_alter_categorytype_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='categorytype',
            name='is_deleted',
        ),
    ]
