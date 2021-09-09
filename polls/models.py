from django.db import models
from django.utils.text import slugify


class Question(models.Model):
    text = models.TextField(max_length=200)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.text[0:10]) + "-" + str(self.id)
            super().save(*args, **kwargs)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

