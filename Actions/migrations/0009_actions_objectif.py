# Generated by Django 3.2.6 on 2021-08-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actions', '0008_alter_actions_date_debut'),
    ]

    operations = [
        migrations.AddField(
            model_name='actions',
            name='objectif',
            field=models.FloatField(default=10000),
            preserve_default=False,
        ),
    ]
