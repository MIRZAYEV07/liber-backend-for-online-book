# Generated by Django 3.2.9 on 2021-12-05 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_recommendation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktype',
            name='price',
            field=models.DecimalField(decimal_places=2, default=12000, max_digits=20),
            preserve_default=False,
        ),
    ]
