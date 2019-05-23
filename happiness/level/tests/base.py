from django.test import TestCase
from level.factories import UserFactory


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('admin123-foo-bar')
        self.user.save()
