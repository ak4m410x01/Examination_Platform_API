from django.db import models
from accounts.models.instructor import Instructor
from levels.models.courses import Course


class Exam(models.Model):
	title = models.CharField(max_length=200)
	instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	course = models.ForeignKey(Course, related_name='exams', on_delete=models.CASCADE)
	exam_score = models.PositiveIntegerField()

	def __str__(self):
		return self.title
