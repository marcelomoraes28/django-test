from datetime import timedelta

from django.utils import timezone

from freezegun import freeze_time
from level.factories import PollFactory


def generate_random_data(days=30):
    """
    Create 300 Poll registers per day in the last 30 days
    0: average -> 3
    1: average -> 3
    2: average -> 3
    3: average -> 3
    4: average -> 2
    5: average -> 3
    6: average -> 3
    7: average -> 2
    8: average -> 2
    9: average -> 3
    10: average -> 3
    11: average -> 3
    12: average -> 3
    13: average -> 3
    14: average -> 3
    15: average -> 3
    16: average -> 3
    17: average -> 4
    18: average -> 3
    19: average -> 3
    20: average -> 3
    21: average -> 3
    22: average -> 2
    23: average -> 3
    24: average -> 3
    25: average -> 3
    26: average -> 2
    27: average -> 2
    28: average -> 2
    29: average -> 3
    """
    _data = {
        0: [2, 2, 3, 5, 2, 1, 2, 4, 3, 4, 3, 4, 5, 3, 5, 4, 1, 4, 5, 1],
        1: [5, 2, 2, 2, 5, 2, 4, 3, 4, 3, 4, 2, 1, 1, 2, 1, 5, 5, 1, 2],
        2: [4, 3, 4, 4, 1, 4, 4, 2, 4, 3, 3, 4, 4, 3, 5, 1, 4, 1, 1, 5],
        3: [1, 3, 2, 2, 5, 2, 2, 5, 2, 1, 5, 1, 3, 3, 5, 4, 5, 1, 4, 2],
        4: [1, 3, 3, 4, 1, 1, 1, 3, 1, 4, 2, 1, 3, 3, 1, 2, 1, 4, 1, 3],
        5: [3, 3, 3, 1, 3, 3, 3, 4, 1, 4, 2, 3, 1, 3, 5, 2, 5, 2, 1, 5],
        6: [4, 1, 2, 1, 1, 3, 3, 2, 2, 1, 4, 5, 1, 3, 3, 5, 1, 4, 3, 2],
        7: [2, 1, 3, 3, 1, 1, 2, 1, 4, 3, 1, 3, 1, 2, 5, 1, 3, 1, 4, 1],
        8: [1, 1, 1, 3, 2, 2, 2, 2, 5, 1, 1, 1, 3, 5, 5, 3, 1, 1, 3, 1],
        9: [2, 3, 3, 5, 2, 5, 1, 1, 1, 5, 5, 1, 4, 1, 5, 2, 3, 5, 1, 5],
        10: [4, 1, 1, 4, 2, 4, 4, 4, 2, 5, 2, 2, 1, 5, 1, 5, 2, 3, 2, 2],
        11: [1, 1, 1, 4, 3, 2, 3, 3, 5, 3, 5, 1, 2, 3, 3, 2, 3, 2, 4, 4],
        12: [1, 4, 1, 4, 4, 3, 1, 5, 5, 2, 5, 1, 4, 1, 3, 4, 1, 1, 1, 5],
        13: [3, 2, 2, 5, 2, 3, 5, 3, 3, 4, 2, 4, 1, 2, 2, 4, 2, 5, 5, 1],
        14: [2, 1, 1, 5, 3, 2, 1, 4, 5, 4, 2, 2, 1, 3, 3, 1, 3, 4, 4, 4],
        15: [1, 1, 1, 3, 5, 3, 5, 1, 4, 4, 4, 2, 5, 4, 3, 3, 1, 1, 3, 1],
        16: [2, 5, 4, 1, 2, 3, 5, 1, 1, 4, 2, 4, 1, 5, 5, 4, 5, 2, 2, 3],
        17: [3, 3, 4, 3, 4, 3, 5, 2, 4, 2, 4, 5, 3, 1, 4, 5, 2, 5, 5, 4],
        18: [1, 4, 5, 4, 5, 3, 4, 3, 2, 2, 5, 2, 2, 5, 2, 4, 5, 2, 3, 3],
        19: [2, 4, 5, 3, 4, 3, 4, 1, 2, 3, 3, 3, 1, 1, 5, 3, 2, 4, 3, 3],
        20: [5, 5, 2, 1, 1, 4, 3, 5, 5, 5, 3, 4, 1, 2, 1, 3, 3, 2, 5, 2],
        21: [1, 5, 5, 1, 4, 3, 4, 5, 2, 1, 5, 4, 3, 3, 2, 2, 3, 5, 1, 5],
        22: [1, 2, 5, 1, 1, 2, 3, 4, 1, 1, 1, 4, 2, 4, 1, 5, 2, 4, 1, 1],
        23: [1, 3, 1, 3, 5, 1, 5, 3, 1, 2, 5, 3, 1, 4, 1, 5, 1, 5, 1, 3],
        24: [1, 3, 4, 1, 5, 2, 4, 2, 3, 2, 4, 5, 3, 3, 2, 1, 1, 4, 1, 3],
        25: [2, 1, 2, 1, 5, 5, 4, 5, 4, 1, 3, 4, 1, 2, 2, 5, 2, 5, 5, 3],
        26: [2, 1, 5, 1, 1, 2, 2, 1, 1, 4, 4, 2, 1, 4, 4, 2, 1, 3, 4, 3],
        27: [3, 5, 3, 1, 5, 1, 3, 1, 1, 1, 5, 4, 1, 5, 1, 1, 1, 2, 2, 1],
        28: [1, 1, 2, 4, 2, 2, 2, 2, 3, 3, 1, 2, 2, 4, 2, 4, 2, 4, 1, 1],
        29: [4, 4, 5, 1, 4, 3, 4, 5, 3, 3, 1, 1, 2, 3, 5, 5, 4, 2, 4, 2]
    }
    for k, v in _data.items():
        if k > days:
            break
        _date = timezone.now() - timedelta(days=k)
        with freeze_time(_date):
            for x in v:
                PollFactory(happy_level=x, date=_date)


def generate_poll_in_the_last_seven_days(user):
    """
    Given a user, polls generated last week
    In this case the average of happy level will be:
        sum([1, 4, 5, 3, 4, 6, 2])/7 = 3.5714285714285716
        round(3.5714285714285716) = 4

    """
    levels = [1, 4, 5, 3, 4, 6, 2]
    for day in range(0, 7):
        _date = timezone.now() - timedelta(days=day)
        with freeze_time(_date):
            PollFactory(user=user, happy_level=levels[day], date=_date)
