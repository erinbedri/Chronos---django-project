# Generated by Django 4.1.1 on 2022-10-07 10:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0017_wpostcomment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WPostComment',
            new_name='PostComment',
        ),
    ]
