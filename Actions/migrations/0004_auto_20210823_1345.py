# Generated by Django 3.2.6 on 2021-08-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actions', '0003_auto_20210823_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='Date_Debut',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='actions',
            name='Date_Fin',
            field=models.DateTimeField(),
        ),
    ]
