from mixer.backend.django import mixer
from django.test import TestCase
from django.core.exceptions import ValidationError
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
    

    def test_person_full_name(self):
        self.assertEqual(
            mixer.blend(Person, first_name="F", last_name="L").full_name, "F L"
        )
        self.assertEqual(
            mixer.blend(Person, first_name="F", last_name="").full_name, "F"
        )
    

    def test_can_get_connections(self):
        p1 = mixer.blend(Person)
        p2 = mixer.blend(Person)
        p3 = mixer.blend(Person)
        p4 = mixer.blend(Person)
        p5 = mixer.blend(Person)
        mixer.blend(Relationship, person1=p1, person2=p2)
        mixer.blend(Relationship, person1=p1, person2=p3)
        mixer.blend(Relationship, person1=p1, person2=p4)
        mixer.blend(Relationship, person1=p3, person2=p5)
        self.assertEqual(set(p1.connections.all()), {p2, p3, p4})
    

    def test_can_list_person_tags(self):
        user = mixer.blend(User)
        p = mixer.blend(Person, user=user)
        tag1 = mixer.blend(Tag, user=user)
        tag2 = mixer.blend(Tag, user=user)
        tag3 = mixer.blend(Tag)
        for tag in [tag1, tag2]: p.tags.add(tag)
        self.assertEqual(set(p.tags.all()), {tag1, tag2})
    

    def test_person_tags_must_have_unique_name(self):
        user = mixer.blend(User)
        mixer.blend(Tag, user=user, name="A")
        mixer.blend(Tag, user=user, name="B")
        mixer.blend(Tag, name="A")
        with self.assertRaises(ValidationError):
            Tag(user=user, name="A").full_clean()



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
    