from django.db import models

# Create your models here.
# name, bio, contact information, profile picture, and areas of expertise.
class Speaker(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    profile_picture = models.CharField(max_length=200)
    reas_of_expertise = models.CharField(max_length=200)
    