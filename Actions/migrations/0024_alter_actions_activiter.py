# Generated by Django 3.2.6 on 2021-09-14 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actions', '0023_actions_activiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='Activiter',
            field=models.CharField(blank=True, default='Rien', max_length=4000),
        ),
    ]
