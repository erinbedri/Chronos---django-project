# Generated by Django 4.1.1 on 2022-10-07 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_rename_wpostcomment_postcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='postcomment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostComment',
        ),
    ]