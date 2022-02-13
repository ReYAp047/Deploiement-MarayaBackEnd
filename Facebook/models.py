from django.db import models

# Create your models here.
class Facebook(models.Model):
    Page_facebook = models.CharField(max_length=1024, blank=False)

    def __str__(self):
        return self.Page_facebook