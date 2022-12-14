# Generated by Django 3.2.9 on 2021-12-03 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='balance', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Balance',
                'verbose_name_plural': 'Balances',
                'ordering': ('id',),
            },
        ),
    ]
