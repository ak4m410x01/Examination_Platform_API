from django.db import models
from exams.models.questions import Question


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.CharField(max_length=200)
	is_correct = models.BooleanField(default=False)

	def __str__(self):
		return self.text
