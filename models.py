from django.db import models

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length = 200)
    location_type = models.CharField(max_length = 200)

    def __str__(self):
        return self.location_name

class Property(models.Model):
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    property_name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    size = models.CharField(max_length = 200)
    age = models.CharField(max_length = 200)
    image_url = models.CharField(max_length = 500)
    lat_value = models.CharField(max_length = 200)
    long_value = models.CharField(max_length = 200)



    def __str__(self):
        return self.property_name




