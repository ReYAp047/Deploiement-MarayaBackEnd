# Generated by Django 3.2.6 on 2021-09-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_Prenom', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('NomAction', models.CharField(max_length=50)),
                ('Montant', models.FloatField()),
                ('Date', models.DateField()),
            ],
        ),
    ]
