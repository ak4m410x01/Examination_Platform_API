"""
This module contains the views for handling questions in the examination platform API.

Classes:
- QuestionListCreate: A view for listing and creating questions.
- QuestionRetrieveUpdateDestroy: A view for retrieving, updating, and deleting questions.
"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from exams.serializers.questions import QuestionSerializer
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isOwner import IsOwner
from accounts.permissions.isStudent import IsStudent
from accounts.permissions.isInstructor import IsInstructor
from exams.models.questions import Question
from django_filters.rest_framework import DjangoFilterBackend
from exams.filters.questions import QuestionsFilter
from authentication.utils.token import JWTToken
from datetime import datetime

class QuestionListCreate(ListCreateAPIView):
    """
    A view for listing and creating questions.

    Attributes:
    - queryset: The queryset of questions to be used for listing.
    - serializer_class: The serializer class for serializing and deserializing questions.

    Methods:
    - get_permissions: Returns the list of permissions required for each HTTP method.
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = QuestionsFilter

    def get_permissions(self):
        """
        Returns the list of permissions required for each HTTP method.

        Returns:
        - A list of permission classes.
        """
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsInstructor | IsStudent)]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsInstructor]
        return super().get_permissions()

    def check_object_permissions(self, request, obj):
        """
        Checks if the user is the owner of the object.

        Args:
        - request: The request object.
        - obj: The object to be checked.

        Returns:
        - None
        """
        super().check_object_permissions(request, obj)

        token = request.auth.token.decode()
        payload = JWTToken.get_payload(token)
        if payload.get("user_role") == "student":
            now = datetime.now()
            if obj.exam.start_time >= now or obj.exam.end_time < now:
                self.permission_denied(request, 'You cannot perform this action at this time.')

class QuestionRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    A view for retrieving, updating, and deleting questions.

    Attributes:
    - queryset: The queryset of questions to be used for retrieval, update, and deletion.
    - serializer_class: The serializer class for serializing and deserializing questions.

    Methods:
    - get_permissions: Returns the list of permissions required for each HTTP method.
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = QuestionsFilter

    def get_permissions(self):
        """
        Returns the list of permissions required for each HTTP method.

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

    def check_object_permissions(self, request, obj):
        """
        Checks if the user is the owner of the object.

        Args:
        - request: The request object.
        - obj: The object to be checked.

        Returns:
        - None
        """
        super().check_object_permissions(request, obj)

        token = request.auth.token.decode()
        payload = JWTToken.get_payload(token)
        if payload.get("user_role") == "student":
            now = datetime.now()
            if obj.exam.start_time >= now or obj.exam.end_time < now:
                self.permission_denied(request, 'You cannot perform this action at this time.')
