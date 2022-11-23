from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Poll
import logging

# Create your views here.
def home(request):
    try:
        polls = Poll.objects.all()
    except Poll.DoesNotExist:
        logging.error('Poll does not exist')
    context = {'polls': polls}
    return render(request, 'poll/home.html', context)


def create (request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {
        'form': form,
    }
    return render(request, 'poll/create.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST.get('poll')
        print(selected_option)
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid Form')

        poll.save()
        return redirect('results', poll.id)
    context = {'poll': poll}
    return render(request, 'poll/vote.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll':poll
    }
    return render(request, 'poll/results.html', context)
