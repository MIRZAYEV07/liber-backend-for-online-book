# Generated by Django 3.2.9 on 2022-08-06 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_auto_20220713_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytype',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_types', to='category.category'),
        ),
    ]
