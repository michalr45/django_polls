# Generated by Django 3.2.7 on 2021-09-17 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_question_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
