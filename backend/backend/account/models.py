from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=4,
        default='None',
        null=True,
        blank=True
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        null=True,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )
    is_active = models.BooleanField(
        default=False,
        null=False,
        blank=False
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    objects = CustomUserManager()

    def __str__(self):
        return self.email