"""Models related to people and their interactions."""

from django.db import models
from core.models import User

class Person(models.Model):
    """A real person in the world, that the user may or not have met, but for
    which they want to be aware of."""

    class Meta:
        db_table = "people"
        verbose_name_plural = "people"
    
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    started = models.DateField(null=True)
    date_of_birth = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="people")



class Tag(models.Model):
    """A tag for categorising people."""

    class Meta:
        db_table = "tags"
        constraints = [
            models.UniqueConstraint(fields=["user", "name"], name="unique name")
        ]

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    people = models.ManyToManyField(Person, related_name="tags", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)