# Generated by Django 3.2.6 on 2021-09-02 16:34

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Actions', '0020_auto_20210902_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='FontImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titre', models.CharField(max_length=50)),
                ('Image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='FontImages')),
            ],
        ),
        migrations.AddField(
            model_name='actions',
            name='Font',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='Actions.fontimages'),
        ),
    ]
