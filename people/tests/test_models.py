from mixer.backend.django import mixer
from django.test import TestCase
from people.models import *

class PersonTests(TestCase):

    def test_can_make_new_person(self):
        kwargs = {
            "last_name": "D", "first_name": "A", "description": "desc",
            "user": mixer.blend(User), "started": "2000-01-01",
            "date_of_birth": "1950-01-01"
        }
        person = Person.objects.create(**kwargs)
        for arg in ["first_name", "description", "started", "date_of_birth"]:
            args = {k: v for k, v in kwargs.items() if k != arg}
            Person.objects.create(**args)