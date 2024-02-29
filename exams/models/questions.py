from django.db import models
from exams.models.exams import Exam


class Question(models.Model):
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	text = models.TextField()

	def __str__(self):
		return self.text
