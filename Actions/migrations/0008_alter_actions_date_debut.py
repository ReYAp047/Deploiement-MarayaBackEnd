# Generated by Django 3.2.6 on 2021-08-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actions', '0007_alter_actions_partonaires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actions',
            name='Date_Debut',
            field=models.DateTimeField(),
        ),
    ]
