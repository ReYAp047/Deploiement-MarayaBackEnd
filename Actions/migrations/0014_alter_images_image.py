# Generated by Django 3.2.6 on 2021-08-28 15:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Actions', '0013_alter_actions_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='Image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='Images'),
        ),
    ]
