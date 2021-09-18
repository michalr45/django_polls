from django import forms
from .models import Question, Answer
from django.forms import modelformset_factory


class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={'class': 'form-control question-form',
                                                 'placeholder': "Enter question",
                                                 'label': 'Poll question'})}


class AnswerModelForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']


AnswerFormset = modelformset_factory(Answer,
                                     fields=['answer_text'],
                                     extra=1,
                                     widgets={'answer_text': forms.TextInput(attrs={'class': 'form-control answer-form',
                                                                                    'placeholder': 'Enter answer',
                                                                                    'label': 'Poll answer'})})
