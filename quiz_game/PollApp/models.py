from django.db import models
from datetime import date

# Create your models here.


class Poll(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(default=date.today())
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Questions(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    true_answer = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title}"


class ChoiceAnswer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.question}"


class Answer(models.Model):
    answer = models.CharField(max_length=100)
    question = models.OneToOneField(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question}"
