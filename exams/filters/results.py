import django_filters
from exams.models import Result

class ResultFilter(django_filters.FilterSet):
	"""
	Filter class for filtering results based on various criteria.

	Attributes:
		student_name (django_filters.CharFilter): Filter for student name.
		exam_title (django_filters.CharFilter): Filter for exam title.
		instructor_name (django_filters.CharFilter): Filter for instructor name.
		min_score (django_filters.NumberFilter): Filter for minimum score.
		max_score (django_filters.NumberFilter): Filter for maximum score.
	"""
	student_name = django_filters.CharFilter(field_name='student__username', lookup_expr='icontains')
	exam_title = django_filters.CharFilter(field_name='exam__title', lookup_expr='icontains')
	instructor_name = django_filters.CharFilter(field_name='exam__instructor__username', lookup_expr='icontains')
	min_score = django_filters.NumberFilter(field_name='score', lookup_expr='gte')
	max_score = django_filters.NumberFilter(field_name='score', lookup_expr='lte')

	class Meta:
		model = Result
		fields = ['student_name', 'exam_title', 'instructor_name', 'min_score', 'max_score']
