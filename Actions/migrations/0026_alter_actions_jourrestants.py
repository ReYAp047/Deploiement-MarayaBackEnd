# Generated by Django 3.2.6 on 2021-09-18 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actions', '0025_actions_jourrestants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='JourRestants',
            field=models.IntegerField(blank=True),
        ),
    ]
