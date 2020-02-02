from mixer.backend.django import mixer
from django.test import TestCase
from people.models import *

class PersonTests(TestCase):

    def test_can_make_new_person(self):
        kwargs = {
            "last_name": "D", "first_name": "A", "description": "desc",
            "user": mixer.blend(User)
        }
        person = Person.objects.create(**kwargs)
        for arg in ["first_name", "description"]:
            args = {k: v for k, v in kwargs.items() if k != arg}
            Person.objects.create(**args)
    

    def test_accounts_are_ordered_correctly(self):
        '''a1 = mixer.blend(Account, name="A")
        mixer.blend(Transaction, account=a1, date="2000-01-08")
        mixer.blend(Transaction, account=a1, date="2000-01-07")
        a2 = mixer.blend(Account, name="C")
        mixer.blend(Transaction, account=a2, date="2000-01-10")
        mixer.blend(Transaction, account=a2, date="2000-01-09")
        a3 = mixer.blend(Account, name="B")
        mixer.blend(Transaction, account=a3, date="2000-01-07", datetime="2000-01-07T03:00:00+00:00")
        a4 = mixer.blend(Account, name="B")
        mixer.blend(Transaction, account=a4, date="2000-01-07", datetime="2000-01-07T06:00:00+00:00")
        a5 = mixer.blend(Account, name="N")
        a6 = mixer.blend(Account, name="M")
        with self.assertNumQueries(1):
            self.assertEqual(list(Account.objects.all()), [a2, a1, a4, a3, a6, a5])
        with self.assertNumQueries(1):
            self.assertEqual(list(Account.objects.filter(name__in="ABNM")), [a1, a4, a3, a6, a5])'''