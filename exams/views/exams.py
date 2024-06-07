"""
This module contains the views for handling exams in the Examination Platform API.

Classes:
- ExamListCreate: Handles the listing and creation of exams.
- ExamRetrieveUpdateDestroy: Handles the retrieval, update, and deletion of exams.
"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from exams.serializers.exams import ExamSerializer
from exams.filters.exams import ExamFilter
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isInstructor import IsInstructor
from accounts.permissions.isStudent import IsStudent
from accounts.permissions.isOwner import IsOwner
from exams.models.exams import Exam


class ExamListCreate(ListCreateAPIView):
    """
    A view for listing and creating exams.

    Attributes:
    - queryset: The queryset of exams to be listed.
    - serializer_class: The serializer class for exams.
    - filter_backends: The filter backends to be used for filtering exams.
    - filterset_class: The filter class for exams.

    Methods:
    - get_permissions: Overrides the default method to set the permissions based on the request method.
    """

    def get_queryset(self):
        user = self.request.user
        print(user)
        if user.is_instructor:
            return Exam.objects.filter(instructor=user)
        elif user.is_student:
            return Exam.objects.filter(Q(students__in=[user]))
        else:
            return Exam.objects.none()

    serializer_class = ExamSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ExamFilter

    def get_permissions(self):
        """
        Sets the permissions based on the request method.

        Returns:
        - A list of permission classes.
        """
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsInstructor | IsStudent)]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsInstructor]
        return super().get_permissions()


class ExamRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    A view for retrieving, updating, and deleting exams.

    Attributes:
    - queryset: The queryset of exams to be retrieved, updated, or deleted.
    - serializer_class: The serializer class for exams.

    Methods:
    - get_permissions: Overrides the default method to set the permissions based on the request method.
    """

    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def get_permissions(self):
        """
        Sets the permissions based on the request method.

        Returns:
        - A list of permission classes.
        """
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsOwner | IsStudent)]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsOwner]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsOwner]
        return super().get_permissions()
