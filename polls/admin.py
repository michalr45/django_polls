from django.contrib import admin
from .models import Question, Answer


class AnswerInLineAdmin(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text']
    inlines = [AnswerInLineAdmin]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'question', 'votes']
