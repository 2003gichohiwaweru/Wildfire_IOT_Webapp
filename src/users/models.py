# app/models.py
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    email_address = models.EmailField()
    gender = models.CharField(max_length=10)
    last_login = models.DateTimeField(auto_now=True)
    employee_number = models.CharField(max_length=6, unique=True, null=True, blank=True)
    date_hired = models.DateField(default=timezone.now, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Greenhouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)  # in square meters
    temperature = models.DecimalField(max_digits=5, decimal_places=2)  # in Celsius
    humidity = models.DecimalField(max_digits=5, decimal_places=2)  # in percentage
    light_intensity = models.DecimalField(max_digits=5, decimal_places=2)  # in lux
    # Add more fields as needed

    def __str__(self):
        return self.name
