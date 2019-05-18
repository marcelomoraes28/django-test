from django.test import TestCase
from level.factories import UserFactory


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
