from level.tests.base import BaseTestCase

from level.tests.populate import generate_poll_in_the_last_seven_days, \
    generate_random_data

from level.models import Poll


class PollTest(BaseTestCase):

    def test_average_of_the_last_seven_days(self):
        """
        First case: Test when just one user voted for one week
            votes: [1, 4, 5, 3, 4, 6, 2]
            average: 3.5714285714285716
            round: 4
        Second case: Test when 20 users voted for one week
            Average per day:
                1: average -> 3
                2: average -> 3
                3: average -> 3
                4: average -> 3
                5: average -> 2
                6: average -> 3
                7: average -> 3
            average: 2,857142857142857
            round: 3
        """
        # First case
        generate_poll_in_the_last_seven_days(user=self.user)
        assert Poll.average_of_the_last_seven_days(user_id=self.user.id) == 4
        assert Poll.average_of_the_last_seven_days() == 4
        # Second case
        generate_random_data(days=7)
        assert Poll.average_of_the_last_seven_days() == 3

    def test_average_per_day(self):
        """
        Case: Test when 20 users voted for one day
            votes: [2, 2, 3, 5, 2, 1, 2, 4, 3, 4, 3, 4, 5, 3, 5, 4, 1, 4, 5, 1]
            average: 3.15
            round: 3
        """
        generate_random_data(days=1)
        assert Poll.average_per_day() == 3
