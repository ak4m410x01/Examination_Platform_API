from django.db import models
from accounts.models import Instructor
from levels.models import Course


class Exam(models.Model):
	title = models.CharField(max_length=200)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()

	def __str__(self):
		return self.title
