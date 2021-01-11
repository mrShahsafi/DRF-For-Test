from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class User(AbstractUser):
    email = models.EmailField(
            unique=True,
            null=False,
            blank=False
                        )


    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
