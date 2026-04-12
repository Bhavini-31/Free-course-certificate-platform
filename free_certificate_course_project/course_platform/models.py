from django.db import models

class Platform(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    logo = models.URLField(blank=True, null=True)  

    def __str__(self):
        return self.name