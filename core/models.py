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






def create_filename(instance, filename):
    extension = "." + filename.split(".")[-1] if "." in filename else ""
    name = instance.name.replace(" ", "_")
    return f"{name.lower()}{extension}"


class Person(models.Model):

    class Meta:
        db_table = "old_people"
        verbose_name_plural = "people"
        ordering = ["last_name"]

    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, blank=True)
    met = models.DateField()
    image = models.FileField(null=True, blank=True, upload_to=create_filename)

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
    description = models.TextField(blank=True)
    person = models.ForeignKey(Person, related_name="interactions", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.name} {self.LEVELS[self.level - 1][1]} on {self.date}"


@receiver(models.signals.post_delete, sender=Person)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes a file when its model is deleted."""

    for attr in ["image"]:
        try:
            if getattr(instance, attr):
                if os.path.isfile(getattr(instance, attr).path):
                    os.remove(getattr(instance, attr).path)
        except: pass
   

@receiver(models.signals.pre_save, sender=Person)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes a file when its model is updated with a new file and changes its
    name if appropriate."""
    
    if not instance.pk: return False
    try:
        db_obj = sender.objects.get(pk=instance.pk)
    except: return False
    
    # Should the name be changed?
    print("Checking")
    for attr in ["name"]:
        try:
            if getattr(db_obj, attr) != getattr(instance, attr):
                for attr2 in ["image"]:
                    print("Updating")
                    try:
                        old_path = getattr(instance, attr2).path
                        new_name = create_filename(instance, getattr(instance, attr2).path)
                        new_path = "/".join(
                         getattr(instance, attr2).path.split("/")[:-1]
                        ) + "/" + new_name
                        print(old_path)
                        print(new_path)
                        os.rename(old_path, new_path)
                        print("Updated")
                        setattr(instance, attr2, new_name)
                    except: pass
        except: pass

    # Should the file be deleted
    for attr in ["image"]:   
        try:
            new_file = getattr(instance, attr)
            if not getattr(db_obj, attr) == new_file:
                if os.path.isfile(getattr(db_obj, attr).path):
                    os.remove(getattr(db_obj, attr).path)

        except: pass