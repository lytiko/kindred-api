import time
from mixer.backend.django import mixer
from django.test import TestCase
from core.models import *
from people.models import Person, Interaction, Relationship, Tag

class UserTests(TestCase):

    def test_can_make_new_user(self):
        user = User.objects.create(email="john@mail.com")
        user.set_password("12345678")
        user.save()
        self.assertNotEqual(user.password, "12345678")
    

    def test_user_tokens(self):
        user = User.objects.create(email="john@mail.com")
        token = user.create_jwt()
        token = jwt.decode(token, settings.SECRET_KEY)
        self.assertEqual(token["sub"], user.id)
        self.assertEqual(token["name"], user.username)
        self.assertLessEqual(time.time() - token["iat"], 2)
    

    def test_can_get_people(self):
        user = mixer.blend(User)
        p1 = mixer.blend(Person, user=user)
        p2 = mixer.blend(Person, user=user)
        p3 = mixer.blend(Person)
        self.assertEqual(list(user.people.all()), [p1, p2])
    

    def test_can_get_interactions(self):
        user = mixer.blend(User)
        i1 = mixer.blend(Interaction, person=mixer.blend(Person, user=user))
        i2 = mixer.blend(Interaction, person=mixer.blend(Person, user=user))
        i3 = mixer.blend(Interaction)
        self.assertEqual(set(user.interactions.all()), {i1, i2})
    

    def test_can_get_relationships(self):
        user = mixer.blend(User)
        person1 = mixer.blend(Person, user=user)
        person2 = mixer.blend(Person, user=user)
        r1 = mixer.blend(Relationship, person1=person1, person2=person2)
        r2 = mixer.blend(Relationship, person1=person1, person2=person2)
        r3 = mixer.blend(Relationship)
        self.assertEqual(set(user.relationships.all()), {r1, r2})
    

    def test_can_get_tags(self):
        user = mixer.blend(User)
        tag1 = mixer.blend(Tag, user=user)
        tag2 = mixer.blend(Tag, user=user)
        tag3 = mixer.blend(Tag)
        self.assertEqual(list(user.tags.all()), [tag1, tag2])