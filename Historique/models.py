from django.db import models
from django.db.models.fields import EmailField

class Historique (models.Model):
    Nom_Prenom = models.CharField(max_length=50,blank=False)
    Email = models.EmailField(max_length=50,blank=False)
    NomAction = models.CharField(max_length=50,blank=False)
    Montant = models.FloatField(blank=False)
    Date = models.DateField(blank=False)

    def __str__(self):
        return self.Email