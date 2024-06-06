"""
This module contains the views for handling results in the Examination Platform API.

Classes:
- ResultListCreate: A view for listing and creating results.
- ResultRetrieveUpdateDestroy: A view for retrieving, updating, and deleting results.
"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from exams.serializers.results import ResultSerializer
from exams.filters.results import ResultFilter
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isOwner import IsOwner
from accounts.permissions.isStudent import IsStudent
from accounts.permissions.isInstructor import IsInstructor
from exams.models.results import Result


class ResultListCreate(ListCreateAPIView):
    """
    A view for listing and creating results.

    Attributes:
    - queryset: The queryset of Result objects.
    - serializer_class: The serializer class for Result objects.
    - filter_backends: The filter backends used for filtering the results.
    - filterset_class: The filter class for filtering the results.

    Methods:
    - get_permissions: Returns the permissions required for different HTTP methods.
    """

    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ResultFilter

    def get_permissions(self):
        """
        Returns the permissions required for different HTTP methods.

        For GET requests, only authenticated admins are allowed.
        For POST requests, only authenticated admins are allowed.

        Returns:
        - A list of permission classes.
        """
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsInstructor | IsStudent)]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsInstructor]
        return super().get_permissions()


class ResultRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    A view for retrieving, updating, and deleting results.

    Attributes:
    - queryset: The queryset of Result objects.
    - serializer_class: The serializer class for Result objects.

    Methods:
    - get_permissions: Returns the permissions required for different HTTP methods.
    """

    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def get_permissions(self):
        """
        Returns the permissions required for different HTTP methods.

        For GET requests, authenticated admins or owners are allowed.
        For PUT requests, only authenticated admins are allowed.
        For DELETE requests, only authenticated admins are allowed.

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
