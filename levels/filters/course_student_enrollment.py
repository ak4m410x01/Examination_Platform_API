import django_filters
from levels.models import CourseStudentEnrollment

class CourseStudentEnrollmentFilter(django_filters.FilterSet):
	student = django_filters.NumberFilter(field_name='student')
	course = django_filters.NumberFilter(field_name='course')
	pass_status = django_filters.BooleanFilter(field_name='pass_status')

	class Meta:
		model = CourseStudentEnrollment
		fields = ['student', 'course', 'pass_status']
