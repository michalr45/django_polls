from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Question(models.Model):
    text = models.TextField(max_length=200)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.text[0:10]) + "-" + str(self.id)
            self.save()

    def get_absolute_url(self):
        return reverse('polls:poll_detail',
                       args=[self.slug])


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)


