"""Core models needed for kindred functionality."""

import os
import jwt
import time
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """The user account model. The email serves as the username."""

    class Meta:
        db_table = "users"

    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def create_jwt(self):
        """Creates a JWT token for the user at the current UTC time.
        
        A JWT token consists of three components, separated by a period.
        
        The first is the header, which lists the algorithm used to encrypt,
        base64 encoded.
        
        The second is the payload, which contains information such as the name
        of the person the token represents, and the time the token was created.
        Again this is a dictionary, base64 encoded.
        
        The third segment is a secret which allows the server to verify that it
        issued this token at some point in the past. The first two sections are
        encrypted using some algorithm and the server's SECRET_KEY. When the
        token is encountered again, the server can confirm that encrypting the
        first two sections does indeed produce the third section."""

        return jwt.encode({
         "sub": self.id, "name": self.username, "iat": int(time.time())
        }, settings.SECRET_KEY, algorithm="HS256").decode()
    

    @property
    def interactions(self):
        """All interaction objects associated with this user."""

        from people.models import Interaction
        return Interaction.objects.filter(person__user=self)
    

    @property
    def relationships(self):
        """All relationship objects associated with this user."""

        from people.models import Relationship
        return Relationship.objects.filter(person1__user=self, person2__user=self)