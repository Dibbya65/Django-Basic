from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
