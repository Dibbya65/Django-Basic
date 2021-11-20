from django.db import models
from django.contrib.auth import User
# Create your models here.


# topic model
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# room model


class Room(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL)
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

# message model


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]
