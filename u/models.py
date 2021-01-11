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
