"""Core models needed for kindred functionality."""

import os
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """The user account model. The email serves as the username."""

    class Meta:
        db_table = "users"

    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []