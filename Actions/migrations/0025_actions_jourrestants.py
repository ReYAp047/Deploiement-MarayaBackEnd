# Generated by Django 3.2.6 on 2021-09-18 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actions', '0024_alter_actions_activiter'),
    ]

    operations = [
        migrations.AddField(
            model_name='actions',
            name='JourRestants',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]