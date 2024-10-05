"""This module contains the signals for creating and saving Client profile."""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Client, Profile


@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    """Create a Client instance when a User is created."""
    if created:
        Client.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_client(sender, instance, **kwargs):
    """Save the Client instance when the User is saved."""
    instance.client.save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a Profile instance when a User is created."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the Profile instance when the User is saved."""
    instance.profile.save()
