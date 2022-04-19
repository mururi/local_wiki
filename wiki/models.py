from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class NeighborHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    name = models.CharField(max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(NeighborHood, null=True, on_delete=models.CASCADE)

