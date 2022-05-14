# Generated by Django 3.2.6 on 2021-09-20 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blogs', '0004_post_moderator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='app_blogs.blog'),
        ),
    ]
