from django.db import models
from destinations.models import Destination

# Create your models here.
class Hotel(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=100)
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    image = models.ImageField(upload_to='hotel_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.destination.name})"