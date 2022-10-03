# Generated by Django 4.1.1 on 2022-10-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_watch_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='style',
            field=models.CharField(choices=[('Pocket', 'Pocket'), ('Railroad', 'Railroad'), ('Dress', 'Dress'), ('Field', 'Field'), ('Aviator', 'Aviator'), ('Dive', 'Dive'), ('Racing', 'Racing'), ('Digital', 'Digital'), ('Smart ', 'Smart'), ('Fashion', 'Fashion')], max_length=8),
        ),
    ]
