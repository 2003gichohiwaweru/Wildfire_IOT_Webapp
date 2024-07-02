from django.db import models
from .consts import GREENHOUSE_NAMES, FLOWER_TYPES, GROWING_STYLE, AREA_SIZE

# Create your models here.
class Greenhouses(models.Model):
    name = models.CharField(max_length=100, choices=GREENHOUSE_NAMES)
    flower_type = models.CharField(choices=FLOWER_TYPES,)
    growing_style = models.CharField(choices=GROWING_STYLE,)
    area = models.CharField(choices=AREA_SIZE)  # in square meters
    temperature = models.DecimalField(max_digits=5, decimal_places=2)  # in Celsius
    humidity = models.DecimalField(max_digits=5, decimal_places=2)  # in percentage
    light_intensity = models.DecimalField(max_digits=5, decimal_places=2)  # in lux
    # Add more fields as needed

    def __str__(self):
        return self.name