"""Models related to people."""

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

    def __str__(self):
        return self.full_name


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
    

    @property
    def connections(self):
        relationships = Relationship.objects.filter(person1=self) | Relationship.objects.filter(person2=self)
        people_ids = [item for sublist in relationships.values_list("person1", "person2") for item in sublist] 
        return Person.objects.filter(id__in=people_ids).exclude(id=self.id)
        
    


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tags")

    def __str__(self):
        return self.name



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
    