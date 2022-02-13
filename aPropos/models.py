from django.db import models

# Create your models here.
class APropos (models.Model):
    A_propos = models.CharField(max_length=2048,blank=False)

    def __str__(self):
        return self.A_propos