from django import forms

from level.models import Poll


class PollForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['happy_level'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Poll
        fields = ['happy_level']
