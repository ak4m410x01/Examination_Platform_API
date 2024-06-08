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
from exams.models.exams import Exam
from django_filters.rest_framework import DjangoFilterBackend
from exams.filters.questions import QuestionsFilter
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

    def get_queryset(self):
        """
        This view should return a list of all the questions
        for the currently authenticated user.
        """
        exam_id = self.request.query_params.get('exam_id', None)
        exam_title = self.request.query_params.get('exam_title', None)
        user_type = self.request.user.user_type

        if exam_id and exam_title:
            if user_type == 3:
                exam = Exam.objects.get(id=exam_id, title=exam_title)
                if not (exam.start_date <= datetime.now() <= exam.end_date):
                    self.permission_denied(self.request, 'You can\'t do that action at this time')
            return Question.objects.filter(exam__id=exam_id, exam__title=exam_title)
        elif user_type == 3:
            self.permission_denied(self.request, 'The parameter exam_id or exam_title or both are missing')
        else:
            return Question.objects.all()

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

class QuestionRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    A view for retrieving, updating, and deleting questions.

    Attributes:
    - queryset: The queryset of questions to be used for retrieval, update, and deletion.
    - serializer_class: The serializer class for serializing and deserializing questions.

    Methods:
    - get_permissions: Returns the list of permissions required for each HTTP method.
    """

    def get_queryset(self):
        """
        This view should return a list of all the questions
        for the currently authenticated user.
        """
        exam_id = self.request.query_params.get('exam_id', None)
        exam_title = self.request.query_params.get('exam_title', None)
        user_type = self.request.user.user_type

        if user_type == 3:
            exam = Exam.objects.get(id=exam_id, title=exam_title)
            if not (exam.start_date <= datetime.now() <= exam.end_date):
                self.permission_denied(self.request, 'You can\'t do that action at this time')

        return Question.objects.all()

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
