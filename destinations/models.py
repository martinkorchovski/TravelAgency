from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='destinations_images')
    duration = models.CharField(max_length=50, default=0)
    rating = models.FloatField(default=5.0)

    def __str__(self):
        return self.name