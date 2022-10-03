# Generated by Django 4.1.1 on 2022-10-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_watch_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='style',
            field=models.CharField(choices=[('Pocket', 'Pocket Watch'), ('Railroad', 'Railroad Watch'), ('Dress', 'Dress Watch'), ('Field', 'Field Watch'), ('Aviator', 'Aviator Watch'), ('Dive', 'Dive Watch'), ('Racing', 'Racing Watch'), ('Digital', 'Digital Watch'), ('Smart ', 'Smart Watch '), ('Fashion', 'Fashion Watch')], max_length=14),
        ),
    ]
