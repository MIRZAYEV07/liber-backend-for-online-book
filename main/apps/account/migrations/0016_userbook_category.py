# Generated by Django 3.2.9 on 2022-02-26 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_alter_categorytype_options'),
        ('account', '0015_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbook',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customer_books', to='category.category'),
            preserve_default=False,
        ),
    ]
