from level.tests.base import BaseTestCase

from level.tests.populate import generate_poll_by_user, generate_random_data

from level.models import Poll


class PollTest(BaseTestCase):

    def test_average_of_the_last_seven_days_one_user(self):
        """
        Case: Test when just one user voted for one week
            votes: [1, 4, 1, 5, 3, 3, 5]
            average: 3.142857142857143
            round: 3
        """
        generate_poll_by_user(user=self.user, days=7)
        assert Poll.average_of_the_last_seven_days(
            team=self.user.team.name) == 3

    def test_average_of_the_last_seven_days_20_user(self):
        """
        Case: Test when 20 users voted for one week
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
        generate_random_data(days=7)
        assert Poll.average_of_the_last_seven_days(
            team=self.user.team.name) == 3

    def test_average_per_day(self):
        """
        Case: Test when 20 users voted for one day
            votes: [2, 2, 3, 5, 2, 1, 2, 4, 3, 4, 3, 4, 5, 3, 5, 4, 1, 4, 5, 1]
            average: 3.15
            round: 3
        """
        generate_random_data(days=1)
        assert Poll.average_per_day(
            team=self.user.team.name) == 3

    def test_average_average_from_the_beginning_by_user(self):
        """
        Case : Test when one user voted for one month
            votes: you can see in module level.tests.populate.generate_poll_by_user
            average: 2.8666666666666667
            round: 3
        """
        generate_poll_by_user(user=self.user)
        assert Poll.average_of_the_last_seven_days(
            team=self.user.team.name) == 3

    def test_average_average_from_the_beginning(self):
        """
        Case : Test when 20 users voted for one month
            votes: you can see in module level.tests.populate.generate_random_data
            averages by day:
                1 -> 3.15
                2 -> 2.8
                3 -> 3.2
                4 -> 2.9
                5 -> 2.15
                6 -> 2.85
                7 -> 2.55
                8 -> 2.15
                9 -> 2.2
                10 -> 3.0
                11 -> 2.8
                12 -> 2.75
                13 -> 2.8
                14 -> 3.0
                15 -> 2.75
                16 -> 2.75
                17 -> 3.05
                18 -> 3.55
                19 -> 3.3
                20 -> 2.95
                21 -> 3.1
                22 -> 3.2
                23 -> 2.3
                24 -> 2.7
                25 -> 2.7
                26 -> 3.1
                27 -> 2.4
                28 -> 2.35
                29 -> 2.25
                30 -> 3.25
            average in 30 days: 2.8
            round: 3
        """
        generate_random_data()
        assert Poll.average_of_the_last_seven_days(
            team=self.user.team.name) == 3
