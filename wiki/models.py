import email
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class NeighborHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null=True)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_neighborhood(self):
        '''
        Method to save a Neighborhood object
        '''
        self.save()

    @classmethod
    def delete_neighborhood(cls, id):
        '''
        Method to delete a Neighborhood object
        '''
        cls.objects.filter(id = id).delete()

    @classmethod
    def find_neigborhood(cls, neigborhood_id):
        '''
        Method to find a Neighborhood bi its id
        '''
        return cls.objects.filter(id = neigborhood_id)[0]

class Profile(models.Model):
    profile_pic = CloudinaryField('image')
    name = models.CharField(max_length=50)
    bio = models.TextField()
    location = models.CharField(max_length=50, null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(NeighborHood, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    email = models.EmailField(max_length=60)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(NeighborHood, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_business(self):
        '''
        Method to save a Business object
        '''
        self.save()

class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(NeighborHood, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
