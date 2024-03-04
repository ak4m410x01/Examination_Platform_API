"""
This module contains the views for handling courses in the Examination Platform API.

Classes:
- CourseListCreate: Handles the listing and creation of courses.
- CourseRetrieveUpdateDestroy: Handles the retrieval, updating, and deletion of a specific course.
"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from levels.serializers.courses import CourseSerializer
from levels.filters.courses import CourseFilter
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isOwner import IsOwner
from levels.models.courses import Course


class CourseListCreate(ListCreateAPIView):
	"""
	View for listing and creating courses.

	Attributes:
	- queryset: The queryset of courses to be used for listing.
	- serializer_class: The serializer class for serializing and deserializing course data.
	- filter_backends: The filter backends to be used for filtering courses.
	- filterset_class: The filter class for applying filters on courses.

	Methods:
	- get_permissions: Overrides the default method to set the appropriate permissions based on the request method.
	"""
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	filter_backends = (DjangoFilterBackend,)
	filterset_class = CourseFilter

	def get_permissions(self):
		"""
		Sets the appropriate permissions based on the request method.

		Returns:
		- A list of permission classes.
		"""
		if self.request.method == "GET":
			self.permission_classes = [IsAuthenticated & IsAdmin]
		elif self.request.method == "POST":
			self.permission_classes = [IsAuthenticated & IsAdmin]
		return super().get_permissions()


class CourseRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
	"""
	View for retrieving, updating, and deleting a specific course.

	Attributes:
	- queryset: The queryset of courses to be used for retrieval, updating, and deletion.
	- serializer_class: The serializer class for serializing and deserializing course data.

	Methods:
	- get_permissions: Overrides the default method to set the appropriate permissions based on the request method.
	"""
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

	def get_permissions(self):
		"""
		Sets the appropriate permissions based on the request method.

		Returns:
		- A list of permission classes.
		"""
		if self.request.method == "GET":
			self.permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]
		elif self.request.method == "PUT":
			self.permission_classes = [IsAuthenticated & IsAdmin]
		elif self.request.method == "DELETE":
			self.permission_classes = [IsAuthenticated & IsAdmin]
		return super().get_permissions()
