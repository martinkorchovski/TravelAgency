from django.db import models
from destinations.models import Destination

# Create your models here.

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    persons = models.IntegerField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
