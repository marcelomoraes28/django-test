from level.tests.base import BaseTestCase
from django.urls import reverse


class PollViewTest(BaseTestCase):
    def setUp(self):
        super(PollViewTest, self).setUp()
        self.client.login(username=self.user.username,
                          password='admin123-foo-bar')

    def test_polls_view_logged(self):
        response = self.client.get(reverse('polls'))
        assert response.status_code == 200

    def test_polls_view_not_logged(self):
        self.client.logout()
        response = self.client.get(reverse('polls'))
        assert response.status_code == 302

    def test_poll_view_logged(self):
        response = self.client.get(reverse('create_poll'))
        assert response.status_code == 200

    def test_poll_view_not_logged(self):
        self.client.logout()
        response = self.client.get(reverse('create_poll'))
        assert response.status_code == 302
