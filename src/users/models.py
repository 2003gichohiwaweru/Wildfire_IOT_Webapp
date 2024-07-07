from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import random
import string

from .consts import GENDER

class Profile(models.Model):
    employee_number = models.CharField(max_length=6, unique=True, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=11)
    email_address = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER)
    last_login = models.DateTimeField(auto_now=True)
    date_hired = models.DateField(default=timezone.now, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    # Add more fields as needed

    def save(self, *args, **kwargs):
        if not self.employee_number:
            self.employee_number = self.generate_unique_employee_number()
        super(Profile, self).save(*args, **kwargs)

    def generate_unique_employee_number(self):
        while True:
            employee_number = ''.join(random.choices(string.digits, k=6))
            if not Profile.objects.filter(employee_number=employee_number).exists():
                return employee_number
            
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
