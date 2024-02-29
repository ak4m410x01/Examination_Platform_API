from django.db import models
from accounts.models.instructor import Instructor
from levels.models.courses import Course


class Exam(models.Model):
	title = models.CharField(max_length=200)
	instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()
	course = models.ForeignKey(Course, related_name='exams', on_delete=models.CASCADE)

	def __str__(self):
		return self.title