import django_filters
from exams.models import StudentAnswer

class StudentAnswersFilter(django_filters.FilterSet):
	"""
	Filter class for filtering student's answers based on various criteria.

	Attributes:
		student (django_filters.CharFilter): Filter for student name.
		exam (django_filters.CharFilter): Filter for exam title.
		question (django_filters.CharFilter): Filter for question text.
	"""
	student_name = django_filters.CharFilter(field_name='student__first_name', lookup_expr='icontains')
	exam = django_filters.CharFilter(field_name='exam__title', lookup_expr='icontains')
	question = django_filters.CharFilter(field_name='question__text', lookup_expr='icontains')

	class Meta:
		model = StudentAnswer
		fields = ['student_name', 'exam', 'question',]
