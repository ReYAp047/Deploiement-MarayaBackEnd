# Generated by Django 3.2.6 on 2021-09-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_Client', models.CharField(max_length=100)),
                ('Message', models.CharField(max_length=1024)),
            ],
        ),
    ]