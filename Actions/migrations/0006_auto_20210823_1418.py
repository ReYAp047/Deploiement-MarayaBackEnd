# Generated by Django 3.2.6 on 2021-08-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actions', '0005_auto_20210823_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='Images',
            field=models.ManyToManyField(to='Actions.Images'),
        ),
        migrations.AlterField(
            model_name='actions',
            name='Videos',
            field=models.ManyToManyField(to='Actions.Videos'),
        ),
    ]
