import jwt
import time
import pytz
import base64
from random import randint
from timezone_field import TimeZoneField
from django.conf import settings
from django.db import models

def create_filename(instance, filename):
    """Creates a filename for some uploaded image, from the owning object's ID,
    and class name."""
    
    extension = "." + filename.split(".")[-1] if "." in filename else ""
    hashed_class = base64.b64encode(instance.__class__.__name__.encode())
    return f"{instance.id}{hashed_class}{extension}"


class BigIdModel(models.Model):
    """Provides a custom ID primary key field - a random 15 digit integer."""

    class Meta:
        abstract = True

    id = models.BigIntegerField(primary_key=True)

    def save(self, *args, **kwargs):
        """If the user hasn't provided an ID, generate one at random and check
        that it has not been taken."""
        
        digits = 18
        if not self.id:
            is_unique = False
            while not is_unique:
                id = randint(10 ** (digits - 1), 10 ** digits)
                is_unique = not self.__class__.objects.filter(id=id).exists()
            self.id = id
        super(BigIdModel, self).save(*args, **kwargs)



class Person(BigIdModel):
    """A person with whom you have some kind of connection."""

    class Meta:
        db_table = "people"
        verbose_name_plural = "people"

    name = models.CharField(max_length=100)
    image = models.FileField(null=True, blank=True, upload_to=create_filename)