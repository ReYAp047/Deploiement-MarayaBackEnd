from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField
# Create your models here.
class Partonaire(models.Model):
    Nom = models.CharField(max_length=50, blank=False)
    Logo = CloudinaryField('Partonaire', blank=False)
    def __str__(self):
        return self.Nom

class Images(models.Model):
    Titre = models.CharField(max_length=50, blank=False)
    Image = CloudinaryField('Images', blank=False)
    def __str__(self):
        return self.Titre

class FontImages(models.Model):
    Titre = models.CharField(max_length=50, blank=False)
    Image = CloudinaryField('FontImages', blank=False)
    def __str__(self):
        return self.Titre

class Videos(models.Model):
    Titre = models.CharField(max_length=50, blank=False)
    Video = CloudinaryField('Videos', blank=False)
    def __str__(self):
        return self.Titre

class Actions(models.Model):
    Nom_Action = models.CharField(max_length=512,blank=False)
    Details = models.CharField(max_length=2048,blank=False)
    Date_Debut = models.DateField(blank=False)
    Date_Fin = models.DateField(blank=False)
    Objectif = models.FloatField(blank=False)
    Atteint = models.FloatField(blank=False)
    Partonaires = models.ManyToManyField(Partonaire, blank=True)
    Font = models.OneToOneField(FontImages, on_delete=models.CASCADE, blank=False, default=None)
    Images = models.ManyToManyField(Images, blank=True)
    Videos = models.ManyToManyField(Videos, blank=True)
    Activiter = models.CharField(max_length=4000,blank=True, default="Rien")
    Terminer = models.BooleanField(default=False)
    JourRestants = models.IntegerField(blank=True)
    def __str__(self):
        return self.Nom_Action
