from django.db import models

class StudentAnswer(models.Model):
	student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
	exam = models.ForeignKey('exams.Exam', on_delete=models.CASCADE)
	question = models.ForeignKey('exams.Question', on_delete=models.CASCADE)
	student_choice = models.ForeignKey('exams.Choice', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('student', 'exam', 'question')

	def __str__(self):
		return f'{self.student} - {self.exam} - {self.question} - {self.student_choice}'
