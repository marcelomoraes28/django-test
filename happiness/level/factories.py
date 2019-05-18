from django.utils import timezone
from django.contrib.auth.models import User
from factory import DjangoModelFactory
from factory import Sequence, SubFactory
from factory.fuzzy import FuzzyChoice

from level.models import Poll


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = Sequence(lambda n: 'user__%d' % n)


class PollFactory(DjangoModelFactory):
    class Meta:
        model = Poll
        django_get_or_create = ('date', 'user')

    user = SubFactory(UserFactory)
    happy_level = FuzzyChoice(['1', '2', '3', '4', '5'])
    date = timezone.now()
