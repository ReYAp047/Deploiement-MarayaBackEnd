# Generated by Django 3.2.6 on 2021-08-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actions', '0016_auto_20210828_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='Partonaires',
            field=models.ManyToManyField(blank=True, to='Actions.Partonaire'),
        ),
    ]