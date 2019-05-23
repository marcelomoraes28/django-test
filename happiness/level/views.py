from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from level.forms import PollForm

from level.models import Poll


class PollView(LoginRequiredMixin, View):
    def post(self, request):
        form = PollForm(request.POST)
        if form.is_valid():
            try:
                poll = form.save(commit=False)
                poll.user = request.user
                poll.save()
                # Just a hack to show the message in view =)
                form.add_error(None, "Thanks for answering.")
            except IntegrityError:
                form.add_error(None,
                               "You already answered the questionnaire today.")
        return render(request, 'poll.html', {'form': form})

    def get(self, request):
        form = PollForm()
        return render(request, 'poll.html', {'form': form})


class PollsView(LoginRequiredMixin, View):

    def get(self, request):
        now = timezone.now()
        my_happiness = Poll.objects.filter(user_id=request.user.id,
                                           date=now).first()
        try:
            team_name = request.user.team.name
            data = {
                "average_per_day": Poll.average_per_day(team=team_name),
                "average_per_week": Poll.average_of_the_last_seven_days(team=team_name),
                "average_from_the_beginning": Poll.average_from_the_beginning(team=team_name),
                "my_happiness": my_happiness.happy_level if my_happiness else 0,
                "total": zip([Poll.total_per_day(team=team_name, level=l[0]) for l in Poll.HAPPY_CHOICES],
                            [Poll.total_of_the_last_seven_days(team=team_name, level=l[0]) for l in Poll.HAPPY_CHOICES],
                            [Poll.total_from_the_beginning(team=team_name, level=l[0]) for l in Poll.HAPPY_CHOICES]),
            }
            return render(request, 'polls.html', data)
        except AttributeError:
            return redirect('home')
