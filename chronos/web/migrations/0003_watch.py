# Generated by Django 4.1.1 on 2022-10-02 19:49

import chronos.web.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('reference_number', models.CharField(max_length=30)),
                ('year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2022)])),
                ('style', models.CharField(choices=[('Pocket Watch', 'Pocket Watch'), ('Railroad Watch', 'Railroad Watch'), ('Dress Watch', 'Dress Watch'), ('Field Watch', 'Field Watch'), ('Aviator Watch', 'Aviator Watch'), ('Dive Watch', 'Dive Watch'), ('Racing Watch', 'Racing Watch'), ('Digital Watch', 'Digital Watch'), ('Smart Watch ', 'Smart Watch '), ('Fashion Watch', 'Fashion Watch')], max_length=14)),
                ('condition', models.TextField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='watch', validators=[chronos.web.validators.file_size])),
            ],
        ),
    ]
