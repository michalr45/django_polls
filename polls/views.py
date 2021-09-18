from django.shortcuts import render, get_object_or_404
from .forms import QuestionModelForm, AnswerFormset
from .models import Question, Answer
from django.shortcuts import redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def create_poll(request):
    if request.method == 'GET':
        question_form = QuestionModelForm(request.GET or None)
        answer_formset = AnswerFormset(queryset=Answer.objects.none())
    elif request.method == 'POST':
        question_form = QuestionModelForm(request.POST)
        answer_formset = AnswerFormset(request.POST)
        if question_form.is_valid() and answer_formset.is_valid():
            question = question_form.save(commit=False)
            if request.user.is_authenticated:
                question.user = request.user
            else:
                question.user = None
            question.save()
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

    if f'vote_cookie_{poll.id}' in request.COOKIES.keys():
        return render(request, 'polls/poll_detail.html', {'poll': poll,
                                                          'answers': answers,
                                                          'error_message': "You already voted!"})
    else:
        try:
            selected_answer = poll.answers.get(pk=request.POST['answer'])
        except(KeyError, Answer.DoesNotExist):
            return render(request, 'polls/poll_detail.html', {'poll': poll,
                                                              'answers': answers,
                                                              'error_message': "Error!"})
        else:
            selected_answer.votes += 1
            selected_answer.save()
            response = HttpResponseRedirect(reverse('polls:poll_results', args=[poll.slug]))
            response.set_cookie(f'vote_cookie_{poll.id}', str(poll.id))
            return response


def poll_results(request, slug):
    poll = get_object_or_404(Question, slug=slug)
    return render(request, 'polls/poll_results.html', {'poll': poll})


@login_required
def polls_dashboard(request):
    polls = Question.objects.filter(user=request.user)
    return render(request, 'polls/polls_dashboard.html', {'polls': polls})


@login_required
def delete_poll(request, slug):
    poll = get_object_or_404(Question, slug=slug)
    poll.delete()
    return redirect('polls:polls_dashboard')
