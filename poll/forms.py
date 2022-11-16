from django.forms import ModelForm
from .models import Poll


class CreatePollForm(ModelForm):
    class Meta: 
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']


# class VoteForm(ModelForm):
#     class Meta:
#         model = Poll
#         fields = [''option_one', 'option_two', 'option_three'']