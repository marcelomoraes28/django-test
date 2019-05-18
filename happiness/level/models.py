from datetime import timedelta
from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg


class Poll(models.Model):
    """
    Poll model
    """
    HAPPY_CHOICES = [
        (1, 1),  # Unhappy =(
        (2, 2),  # A little bit Unhappy  =\
        (3, 3),  # It's fine =}
        (4, 4),  # Today is a good day =]
        (5, 5),  # Oh my good I won the lottery =DD
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    def average_per_day(cls):
        """
        Calculate the average per day
        Rules: The value will be round.
        Eg:
            1.4 = 1
            1.5 = 1
            1.6 = 2
            1.7 = 2
        :return: integer number between 1 and 5
        """
        now = timezone.now()

        avg = cls.objects.filter(date=now).aggregate(
            avg=Avg('happy_level')).get('avg', 0)
        return round(avg) if avg else 0

    @classmethod
    def average_of_the_last_seven_days(cls, user_id=None):
        """
        Calculate the average between the last seven days
            Eg:
            1.4 = 1
            1.5 = 1
            1.6 = 2
            1.7 = 2
        :param user_id: not required
        :return: integer number between 1 and 5
        """
        now = timezone.now()
        seven_days_ago = now - timedelta(days=7)
        if user_id:
            # Bring average informed user
            avg = cls.objects.filter(date__range=[seven_days_ago, now],
                                     user_id=user_id).aggregate(
                avg=Avg('happy_level')).get('avg', 0)
        else:
            avg = cls.objects.filter(
                date__range=[seven_days_ago, now]).aggregate(
                avg=Avg('happy_level')).get('avg', 0)
        return round(avg) if avg else 0
