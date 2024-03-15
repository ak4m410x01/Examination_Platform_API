from django.db import models
from levels.models.courses import Course


class CourseStudentEnrollment(models.Model):
	student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	pass_status = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.student} enrolled in {self.course}'
