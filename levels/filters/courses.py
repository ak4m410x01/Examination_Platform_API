import django_filters
from levels.models import Course

class CourseFilter(django_filters.FilterSet):
	"""
	Filter class for Course model.

	Available filters:
	- course_code: Filter by course code (exact match).
	- title: Filter by course title (exact match).
	- description: Filter by course description (case-insensitive contains match).
	- duration: Filter by course duration (exact match).
	- level: Filter by course level (exact match).
	- instructor: Filter by instructor ID (exact match).
	- students: Filter by student IDs (exact match, multiple values allowed).

	Usage example:
	filter = CourseFilter(data=request.GET, queryset=Course.objects.all())
	filtered_courses = filter.qs
	"""

	course_code = django_filters.CharFilter(field_name='course_code')
	title = django_filters.CharFilter(field_name='title')
	description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')
	duration = django_filters.DurationFilter(field_name='duration')
	level = django_filters.NumberFilter(field_name='level')
	instructor = django_filters.NumberFilter(field_name='instructor')
	students = django_filters.ModelMultipleChoiceFilter(field_name='students', to_field_name='id')

	class Meta:
		model = Course
		fields = ['course_code', 'title', 'description', 'duration', 'level', 'instructor', 'students']
