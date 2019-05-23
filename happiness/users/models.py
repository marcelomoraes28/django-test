from django.contrib.auth.models import AbstractUser
from django.db import models


class Team(models.Model):
    """
    Team model
    """
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=1024)


class CustomUser(AbstractUser):
    """
    Custom User model
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True,
                             null=True)
