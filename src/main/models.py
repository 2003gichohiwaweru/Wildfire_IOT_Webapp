from django.db import models
from .consts import GREENHOUSE_NAMES, FLOWER_TYPES, GROWING_STYLE, AREA_SIZE
from users.models import Profile
import random
import string

# Create your models here.
class Greenhouses(models.Model):
    greenhouse_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, choices=GREENHOUSE_NAMES, default=GREENHOUSE_NAMES[0])
    flower_type = models.CharField(choices=FLOWER_TYPES, default=FLOWER_TYPES[0])
    growing_style = models.CharField(choices=GROWING_STYLE, default=GROWING_STYLE[0])
    area = models.CharField(choices=AREA_SIZE, default=AREA_SIZE[0])  # in square meters
    temperature = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # in Celsius
    humidity = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # in percentage
    light_intensity = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # in lux
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

   

    def __str__(self):
        return self.name
