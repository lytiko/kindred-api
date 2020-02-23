from mixer.backend.django import mixer
from django.test import TestCase
from django.core.exceptions import ValidationError
from relationships.models import *
from people.models import Person

class InteractionTests(TestCase):

    def test_can_make_new_interaction(self):
        kwargs = {
            "date": "2000-01-01", "person": mixer.blend(Person),
            "description": "chat", "level": 1
        }
        interaction = Interaction.objects.create(**kwargs)
        for arg in ["description"]:
            args = {k: v for k, v in kwargs.items() if k != arg}
            Interaction.objects.create(**args)
    

    def test_interactions_ordered_correctly(self):
        i1 = mixer.blend(Interaction, date="2000-01-03")
        i2 = mixer.blend(Interaction, date="2000-01-01")
        i3 = mixer.blend(Interaction, date="2000-01-02")
        self.assertEqual(list(Interaction.objects.all()), [i2, i3, i1])