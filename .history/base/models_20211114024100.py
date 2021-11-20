from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    Active = 'Active'
    Deactive = 'Deactive'
    STATUS_CHOICE = ((Active, Active), (Deactive, Deactive))
    status = models.CharField(choices=STATUS_CHOICE, default=Deactive)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
