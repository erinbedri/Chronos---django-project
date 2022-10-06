# Generated by Django 4.1.1 on 2022-10-06 14:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0013_alter_watch_condition_alter_watch_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='likes',
            field=models.ManyToManyField(related_name='watch_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
