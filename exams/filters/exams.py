import django_filters
from exams.models.exams import Exam


class ExamFilter(django_filters.FilterSet):
	title = django_filters.CharFilter("title", lookup_expr="icontains")
	instructor = django_filters.CharFilter("instructor", lookup_expr="icontains")
	start_date = django_filters.CharFilter("start_date", lookup_expr="icontains")
	end_date = django_filters.CharFilter("end_date", lookup_expr="icontains")
	course = django_filters.CharFilter("course", lookup_expr="icontains")
	student = django_filters.CharFilter(method="filter_by_student")
	level = django_filters.CharFilter(method="filter_by_level")
	department = django_filters.CharFilter(method="filter_by_department")
	results = django_filters.CharFilter(method="filter_by_results")

	def filter_by_student(self, queryset, name, value):
		"""
		Filter the queryset by student name.

		This method is used to filter a queryset based on a student's name.
		The queryset parameter represents the initial queryset that needs
		to be filtered. The name parameter is not used in the method,
		so it can be ignored for now. The value parameter represents
		the name of the student that we want to filter by.

		Inside the method, the filter() function is used on the queryset
		to apply a filter condition. The filter condition is specified
		as students__name__icontains=value. Let's break down this filter condition:

		students is a related field that represents the students enrolled in the exam.
		name is a field on the student model that represents the name of the student.
		icontains is a case-insensitive containment lookup that checks if the
		value provided is contained within the name field.

		Arguments:
			queryset (QuerySet): The queryset to filter.
			name (str): The name of the filter.
			value (str): The value to filter by.

		Returns:
			QuerySet: The filtered queryset.
		"""
		return queryset.filter(students__username__exact=value)

	def filter_by_level(self, queryset, name, value):
		"""
		Filter the queryset by level name.

		This method is used to filter a queryset based on a level's name.
		The queryset parameter represents the initial queryset that needs
		to be filtered. The name parameter is not used in the method,
		so it can be ignored for now. The value parameter represents
		the name of the level that we want to filter by.

		Inside the method, the filter() function is used on the queryset
		to apply a filter condition. The filter condition is specified
		as level__name__icontains=value. Let's break down this filter condition:

		level is a related field that represents the level associated with the exam.
		name is a field on the level model that represents the name of the level.
		icontains is a case-insensitive containment lookup that checks if the
		value provided is contained within the name field.

		Arguments:
			queryset (QuerySet): The queryset to filter.
			name (str): The name of the filter.
			value (str): The value to filter by.

		Returns:
			QuerySet: The filtered queryset.
		"""
		return queryset.filter(level__name__icontains=value)

	def filter_by_department(self, queryset, name, value):
		"""
		Filter the queryset by department name.

		This method is used to filter a queryset based on a department's name.
		The queryset parameter represents the initial queryset that needs
		to be filtered. The name parameter is not used in the method,
		so it can be ignored for now. The value parameter represents
		the name of the department that we want to filter by.

		Inside the method, the filter() function is used on the queryset
		to apply a filter condition. The filter condition is specified
		as course__department__name__icontains=value. Let's break down this filter condition:

		course is a related field that represents the course associated with the department.
		department is a related field that represents the department associated with the course.
		name is a field on the department model that represents the name of the department.
		icontains is a case-insensitive containment lookup that checks if the
		value provided is contained within the name field.

		Arguments:
			queryset (QuerySet): The queryset to filter.
			name (str): The name of the filter.
			value (str): The value to filter by.

		Returns:
			QuerySet: The filtered queryset.
		"""
		return queryset.filter(course__level__department__name__icontains=value)

	def filter_by_results(self, queryset, name, value):
		"""
		Filter the queryset by results.

		This method is used to filter a queryset based on the results of the exam.
		The queryset parameter represents the initial queryset that needs
		to be filtered. The name parameter is not used in the method,
		so it can be ignored for now. The value parameter represents
		the results that we want to filter by.

		Inside the method, the filter() function is used on the queryset
		to apply a filter condition. The filter condition is specified
		as results__icontains=value. Let's break down this filter condition:

		results is a related field that represents the results associated with the exam.
		icontains is a case-insensitive containment lookup that checks if the
		value provided is contained within the results field.

		Arguments:
			queryset (QuerySet): The queryset to filter.
			name (str): The name of the filter.
			value (str): The value to filter by.

		Returns:
			QuerySet: The filtered queryset.
		"""
		return queryset.filter(results__icontains=value)

	class Meta:
		model = Exam
		fields = [
			"title",
			"start_date",
			"end_date",
			"course",
			"instructor",
			"student",
			"level",
			"department",
			"results",
		]
