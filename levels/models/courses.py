from django.db import models
from accounts.models.instructor import Instructor
from levels.models.levels import Level


class Course(models.Model):
	course_code = models.CharField(max_length=20)
	title = models.CharField(max_length=200)
	description = models.TextField()
	duration = models.PositiveIntegerField()
	level = models.ForeignKey(Level, on_delete=models.CASCADE)
	instructor = models.ForeignKey(Instructor, related_name='courses', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.title} code: {self.course_code}'
