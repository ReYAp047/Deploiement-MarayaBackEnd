# Generated by Django 3.2.6 on 2021-08-23 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APropos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aPropos', models.CharField(max_length=2048)),
                ('Afficher', models.BooleanField(default=False)),
            ],
        ),
    ]