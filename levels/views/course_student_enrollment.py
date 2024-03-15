"""
This module contains the views for managing course student enrollments.
"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from levels.serializers.course_student_enrollment import CourseStudentEnrollmentSerializer
from levels.filters.course_student_enrollment import CourseStudentEnrollmentFilter
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isOwner import IsOwner
from levels.models.course_student_enrollment import CourseStudentEnrollment


class CourseStudentEnrollmentListCreate(ListCreateAPIView):
    """
    A view for listing and creating course student enrollments.

    Inherits from ListCreateAPIView class provided by Django REST Framework.
    """

    queryset = CourseStudentEnrollment.objects.all()
    serializer_class = CourseStudentEnrollmentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CourseStudentEnrollmentFilter

    def get_permissions(self):
        """
        Returns the list of permissions required for the view based on the request method.

        For GET and POST requests, the user must be authenticated and an admin.
        """
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()


class CourseStudentEnrollmentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    A view for retrieving, updating, and deleting a course student enrollment.

    Inherits from RetrieveUpdateDestroyAPIView class provided by Django REST Framework.
    """

    queryset = CourseStudentEnrollment.objects.all()
    serializer_class = CourseStudentEnrollmentSerializer

    def get_permissions(self):
        """
        Returns the list of permissions required for the view based on the request method.

        For GET requests, the user must be authenticated and either an admin or the owner of the enrollment.
        For PUT and DELETE requests, the user must be authenticated and an admin.
        """
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()
