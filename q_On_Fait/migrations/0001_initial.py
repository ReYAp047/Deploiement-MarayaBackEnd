# Generated by Django 3.2.6 on 2021-08-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Q_On_Fait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q_On_Fait', models.CharField(max_length=2048)),
            ],
        ),
    ]
