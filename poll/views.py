from django.shortcuts import render
from .forms import CreatePollForm
from .models import Poll

# Create your views here.
def home(request):
    context = {}
    return render(request, 'poll/home.html', context)


def create (request):
    form = CreatePollForm()
    context = {
        'form': form,
    }
    return render(request, 'poll/create.html', context)


def vote(request, poll_id):
    context = {}
    return render(request, 'poll/vote.html', context)


def results(request, poll_id):
    context = {}
    return render(request, 'poll/results.html', context)