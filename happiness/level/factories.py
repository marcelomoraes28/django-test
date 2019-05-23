from django.utils import timezone
from factory import DjangoModelFactory
from factory import Sequence, SubFactory
from factory.fuzzy import FuzzyChoice

from level.models import Poll
from users.models import CustomUser, Team


class TeamFactory(DjangoModelFactory):
    class Meta:
        model = Team

    name = Sequence(lambda n: 'team__%d' % n)
    description = Sequence(lambda n: 'team__description__%d' % n)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser
        django_get_or_create = ('username',)

    username = Sequence(lambda n: 'user__%d' % n)
    team = SubFactory(TeamFactory)


class PollFactory(DjangoModelFactory):
    class Meta:
        model = Poll
        django_get_or_create = ('date', 'user')

    user = SubFactory(UserFactory)
    happy_level = FuzzyChoice(['1', '2', '3', '4', '5'])
    date = timezone.now()
