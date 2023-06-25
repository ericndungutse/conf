from django.db import models

# Create your models here.
# name, category, date, venue, and theme
class Conference(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    date = models.DateTimeField("date of conference")
    theme = models.CharField(max_length=200)

