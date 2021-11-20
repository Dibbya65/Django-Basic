from django.db import models
# Create your models here.

# room model


class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    Active = 'Active'
    Deactive = 'Deactive'
    STATUS_CHOICE = ((Active, Active), (Deactive, Deactive))
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICE, default=Deactive)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # string representation
    def __str__(self):
        return self.name

# team portfolio
