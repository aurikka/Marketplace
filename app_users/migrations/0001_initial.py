# Generated by Django 3.2.6 on 2021-09-23 08:19

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=Decimal('100000'), max_digits=12, verbose_name='balance')),
                ('loyal_points', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='loyal_points')),
                ('status', models.CharField(choices=[('B', 'Bronze'), ('S', 'Silver'), ('G', 'GOLD')], default='B', max_length=1, verbose_name='status')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]
