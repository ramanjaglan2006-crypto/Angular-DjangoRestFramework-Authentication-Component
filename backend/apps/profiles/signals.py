from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from apps.profiles.models import Profile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a profile automatically when a user is created.
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal to save the profile when the user is saved.
    """
    if hasattr(instance, 'profile'):
        instance.profile.save()
