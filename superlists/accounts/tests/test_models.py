from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):

    def test_user_is_valid_with_email_only(self):
        user = User(email='a@b.com')
        user.full_clean()  # should not raise

    def test_email_is_primary_key(self):
        user = User(email='a@b.com')
        self.assertEqual(user.pk, 'a@b.com')
