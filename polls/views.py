from django.shortcuts import render
from .forms import QuestionModelForm, AnswerModelForm, AnswerFormset
from .models import Question, Answer
from django.shortcuts import redirect


def create_poll(request):
    if request.method == 'GET':
        question_form = QuestionModelForm(request.GET or None)
        answer_formset = AnswerFormset(queryset=Answer.objects.none())
    elif request.method == 'POST':
        question_form = QuestionModelForm(request.POST)
        answer_formset = AnswerFormset(request.POST)
        if question_form.is_valid() and answer_formset.is_valid():
            question = question_form.save()
            for form in answer_formset:
                answer = form.save(commit=False)
                answer.question = question
                answer.save()
            return redirect('/')
    return render(request, 'polls/create_poll.html', {'question_form': question_form,
                                                      'answer_formset': answer_formset})



