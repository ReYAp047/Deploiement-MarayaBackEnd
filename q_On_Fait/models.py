from django.db import models

# Create your models here.
class Q_On_Fait (models.Model):
    Q_On_Fait = models.CharField(max_length=2048,blank=False)

    def __str__(self):
        return self.Q_On_Fait