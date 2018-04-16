from django.test import TestCase
import datetime
from users.templatetags.user_filters import allowed, bizzfuzz
from .models import CustomUser

class CustomUserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(username="test5", password="123", birth_date=datetime.datetime(2010, 1, 1), random_number=30)
        CustomUser.objects.create(username="test6", password="123", birth_date=datetime.datetime(2001, 1, 1), random_number=5)

    def test_user_allowed(self):
        user = CustomUser.objects.get(username="test5")
        user2 = CustomUser.objects.get(username="test6")
        self.assertEqual(allowed(user.birth_date), 'blocked')
        self.assertEqual(allowed(user2.birth_date), 'allowed')

    def test_user_bizzfuzz(self):
        user = CustomUser.objects.get(username="test5")
        user2 = CustomUser.objects.get(username="test6")
        self.assertEqual(bizzfuzz(user.random_number), 'BizzFuzz')
        self.assertEqual(bizzfuzz(user2.random_number), 'Fuzz')
