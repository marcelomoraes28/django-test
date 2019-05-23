from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.db.models import Avg

from users.models import CustomUser


class Poll(models.Model):
    """
    Poll model
    """
    HAPPY_CHOICES = [
        ('1', '1'),  # Unhappy =(
        ('2', '2'),  # A little bit Unhappy  =\
        ('3', '3'),  # It's fine =}
        ('4', '4'),  # Today is a good day =]
        ('5', '5'),  # Oh my good I won the lottery =DD
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    happy_level = models.CharField(max_length=1,
                                   choices=HAPPY_CHOICES)
    date = models.DateField(auto_now_add=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'date']
        # Add index's for searches to be quick
        indexes = [
            models.Index(fields=['happy_level', 'date']),
            models.Index(fields=['happy_level', 'date', 'user']),
            models.Index(fields=['happy_level']),
        ]

    @classmethod
    def average_per_day(cls, team):
        """
        Calculate the average per day
        Rules: The value will be round.
        Eg:
            if the average is 1.4 then it will be rounded to 1
            if the average is 1.6 then it will be rounded to 2
        :param team: group that the user belongs to
        :return: integer number between 1 and 5
        """
        now = timezone.now()

        avg = cls.objects.filter(date=now,
                                 user__team__name=team).aggregate(
            avg=Avg('happy_level')).get('avg', 0)
        return round(avg) if avg else 0

    @classmethod
    def average_of_the_last_seven_days(cls, team):
        """
        Calculate the average between the last seven days
            Eg:
            if the average is 1.4 then it will be rounded to 1
            if the average is 1.6 then it will be rounded to 2
        :param team: group that the user belongs to
        :return: integer number between 1 and 5
        """
        now = timezone.now()
        seven_days_ago = now - timedelta(days=7)
        avg = cls.objects.filter(
            date__range=[seven_days_ago, now],
            user__team__name=team).aggregate(
            avg=Avg('happy_level')).get('avg', 0)
        return round(avg) if avg else 0

    @classmethod
    def average_from_the_beginning(cls, team):
        """
        Calculate the average from the beginning
            Eg:
            if the average is 1.4 then it will be rounded to 1
            if the average is 1.6 then it will be rounded to 2
        :param team: group that the user belongs to
        :return: integer number between 1 and 5
        """

        avg = cls.objects.filter(
            user__team__name=team).aggregate(
            avg=Avg('happy_level')).get(
            'avg', 0)
        return round(avg) if avg else 0

    @classmethod
    def total_per_day(cls, team, level):
        """
        Count the total number of people voting at the level informed today
        :param team:
        :param level: 1,2,3,4,5
        :return:
        """
        now = timezone.now()
        total = cls.objects.filter(date=now,
                                   user__team__name=team,
                                   happy_level=str(level)).count()
        return total

    @classmethod
    def total_of_the_last_seven_days(cls, team, level):
        """
        Count the total number of people voting at the level informed between
        the last seven days
        :param team:
        :param level: 1,2,3,4,5
        :return:
        """
        now = timezone.now()
        seven_days_ago = now - timedelta(days=7)
        total = cls.objects.filter(
            date__range=[seven_days_ago, now],
            user__team__name=team,
            happy_level=level).count()
        return total

    @classmethod
    def total_from_the_beginning(cls, team, level):
        """
        Count the total number of people voting at the level informed
        :param team:
        :param level: 1,2,3,4,5
        :return:
        """

        total = cls.objects.filter(
            user__team__name=team,
            happy_level=level).count()
        return total
