from django.contrib.auth.models import User
from django.db import models


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
    date = models.DateField(auto_created=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'date']
