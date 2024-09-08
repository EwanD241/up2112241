from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Creates a class to store the entries
class Entries(models.Model):
    #Defines the title of the entry, as a max of 255 characters
    title = models.CharField(max_length=255)
    #Determines the start date of the entry
    start = models.DateField()
    #Determines the end date of the entry
    end = models.DateField()
    #Defines the logged in user and deletes their entries when the user is deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='events')

    #Returns the title as a string
    def __str__(self):
        return self.title