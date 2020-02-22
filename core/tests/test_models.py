from mixer.backend.django import mixer
from django.test import TestCase
from core.models import *
from people.models import Tag

class UserTests(TestCase):

    def test_can_make_new_user(self):
        user = User.objects.create(email="john@mail.com")
        user.set_password("12345678")
        user.save()
        self.assertNotEqual(user.password, "12345678")
    

    def test_can_get_tags(self):
        user = mixer.blend(User)
        tag1 = mixer.blend(Tag, user=user)
        tag2 = mixer.blend(Tag, user=user)
        tag3 = mixer.blend(Tag)
        self.assertEqual(list(user.tags.all()), [tag1, tag2])