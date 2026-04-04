from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title