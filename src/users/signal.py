
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from main.models import Greenhouses  # Import the Greenhouses model
from main.consts import GREENHOUSE_NAMES, FLOWER_TYPES, GROWING_STYLE, AREA_SIZE  # Import constants

# Signal to create a Profile instance when a User instance is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # Create a Greenhouse instance for the new Profile
        


