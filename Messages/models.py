from django.db import models

# Create your models here.
class Message(models.Model):
    Email_Client = models.CharField(max_length=100, blank=False)
    Message = models.CharField(max_length=1024, blank=False)
    def __str__(self):
        return self.Email_Client