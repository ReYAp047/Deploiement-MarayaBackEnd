# Generated by Django 3.2.6 on 2021-09-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actions', '0019_auto_20210902_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='Date_Debut',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='actions',
            name='Date_Fin',
            field=models.DateField(),
        ),
    ]
