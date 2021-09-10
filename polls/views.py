from django.shortcuts import render, get_object_or_404
from .forms import QuestionModelForm, AnswerModelForm, AnswerFormset
from .models import Question, Answer
from django.shortcuts import redirect, HttpResponseRedirect
from django.urls import reverse


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
            return redirect(question.get_absolute_url())
    return render(request, 'polls/create_poll.html', {'question_form': question_form,
                                                      'answer_formset': answer_formset})


def poll_detail(request, slug):
    poll = get_object_or_404(Question, slug=slug)
    answers = poll.answers.all()

    return render(request, 'polls/poll_detail.html', {'poll': poll,
                                                      'answers': answers})


def poll_vote(request, slug):
    poll = get_object_or_404(Question, slug=slug)
    answers = poll.answers.all()

    try:
        selected_answer = poll.answers.get(pk=request.POST['answer'])
    except(KeyError, Answer.DoesNotExist):
        return render(request, 'polls/poll_detail.html', {'poll': poll,
                                                          'answers': answers,
                                                          'error_message': "Error!"})
    else:
        selected_answer.votes += 1
        selected_answer.save()
        return HttpResponseRedirect(reverse('polls:poll_results', args=[poll.slug]))


def poll_results(request, slug):
    poll = get_object_or_404(Question, slug=slug)
    return render(request, 'polls/poll_results.html', {'poll': poll})
