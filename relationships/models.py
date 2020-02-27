"""Models related to the interactions and relations between people."""

from django.db import models
from people.models import Person

class Interaction(models.Model):
    """An interaction with a person."""

    class Meta:
        db_table = "interactions"
        ordering = ["date"]
    
    LEVELS = [
        (1, "Text"),
        (2, "Voice"),
        (3, "In Person"),
    ]
    
    date = models.DateField()
    level = models.IntegerField(choices=LEVELS)
    description = models.TextField(blank=True)
    person = models.ForeignKey(Person, related_name="interactions", on_delete=models.CASCADE)



class Relationship(models.Model):
    """An relationship between two people."""

    class Meta:
        db_table = "relationships"

    description = models.TextField(blank=True)
    person1 = models.ForeignKey(Person, related_name="_relationships1", on_delete=models.CASCADE)
    person2 = models.ForeignKey(Person, related_name="_relationships2", on_delete=models.CASCADE)
    