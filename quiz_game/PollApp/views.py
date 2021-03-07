from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


def home(request):
    return render(request, 'PollApp/home.html')


def geo_questions(request):
    question = ChoiceAnswer.objects.all()
    context = {'question': question}
    return render(request, 'PollApp/geo_questions.html', context)


def math_questions(request):
    return render(request, 'PollApp/math_questions.html')


def answer(request, i_id):
    question = ChoiceAnswer.objects.get(id = i_id)
    form = AnswerForm(initial={'question': question})
    context = {'question': question, 'form': form}
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer'] == Questions.true_answer:
                Poll.points += 1
            form.save()
        return redirect('geo_questions')
    return render(request, 'PollApp/answer.html', context)
