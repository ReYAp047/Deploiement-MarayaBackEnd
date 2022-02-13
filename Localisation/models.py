from django.db import models

# Create your models here.
class Localisation (models.Model):
    Localisation = models.CharField(max_length=1024,blank=False)

    def __str__(self):
        return self.Localisation