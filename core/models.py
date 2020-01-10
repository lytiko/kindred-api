from django.db import models

class Person(models.Model):

    class Meta:
        db_table = "people"
        verbose_name_plural = "people"
        ordering = ["last_name"]

    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, blank=True)
    met = models.DateField()

    def __str__(self):
        return self.name
    

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    

    @property
    def last_interaction(self):
        return self.interactions.last()
    

    @property
    def last_voice_interaction(self):
        return self.interactions.filter(level__gt=1).last()
    

    @property
    def last_person_interaction(self):
        return self.interactions.filter(level__gt=2).last()




class Interaction(models.Model):

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
    description = models.TextField()
    person = models.ForeignKey(Person, related_name="interactions", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.name} {self.LEVELS[self.level - 1][1]} on {self.date}"