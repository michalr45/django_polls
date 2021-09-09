from django import forms
from .models import Question, Answer
from django.forms import modelformset_factory


class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {'text': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Enter Question'})}


class AnswerModelForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']


AnswerFormset = modelformset_factory(Answer,
                                     fields=['answer_text'],
                                     extra=1,
                                     widgets={'answer_text': forms.TextInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'Enter answer'})})

