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
from exams.models.questions import Question


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

    def get_permissions(self):
        """
        Returns the list of permissions required for each HTTP method.

        Returns:
        - A list of permission classes.
        """
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()


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

    def get_permissions(self):
        """
        Returns the list of permissions required for each HTTP method.

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
