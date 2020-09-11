import os
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from core.models import Person

class PersonTest(TestCase):

    def setUp(self):
        self.upload_files = os.listdir("uploads")
    

    def tearDown(self):
        for f in os.listdir("uploads"):
            if f not in self.upload_files:
                os.remove(os.path.join("uploads", f))



class PersonCreationTests(PersonTest):

    def test_can_create_person(self):
        kwargs = {"name": "John Locke", "image": SimpleUploadedFile(
            "pic.png", b"contents", content_type="image/png"
        )}
        person = Person.objects.create(**kwargs)
        person.full_clean()
        self.assertNotEqual(person.id, 1)
        self.assertTrue(person.image.name.endswith("bUGVyc29u.png"))
        for arg in ["name"]:
            args = {k: v for k, v in kwargs.items() if k != arg}
            with self.assertRaises(Exception):
                Person.objects.create(**args).full_clean()
    

    def test_can_create_person_minimal_values(self):
        kwargs = {"name": "John Locke"}
        person = Person.objects.create(**kwargs)
        defaults = {"image": None}
        for arg in defaults:
            args = {k: v for k, v in kwargs.items() if k != arg}
            person = Person.objects.create(**args)
            person.full_clean()
            self.assertEqual(getattr(person, arg), defaults[arg])