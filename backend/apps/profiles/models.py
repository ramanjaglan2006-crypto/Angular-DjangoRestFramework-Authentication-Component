from django.db import models
from django.conf import settings
from apps.core.models import BaseModel

class Profile(BaseModel):
    """
    User profile model.
    Stores additional information about the user.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    avatar_url = models.URLField(
        max_length=1024,
        blank=True,
        null=True,
        verbose_name="Avatar URL"
    )
    title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Title"
    )
    bio = models.TextField(
        blank=True,
        verbose_name="Biography"
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Phone Number"
    )

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"Profile for {self.user.username}"
