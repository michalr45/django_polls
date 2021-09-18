from django import template

register = template.Library()


@register.simple_tag
def get_top_answer(poll):
    sorted_answers = poll.answers.order_by('-votes')
    top_answer = sorted_answers[0].answer_text
    return top_answer
