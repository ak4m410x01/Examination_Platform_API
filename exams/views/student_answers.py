from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isOwner import IsOwner
from accounts.permissions.isStudent import IsStudent
from accounts.permissions.isInstructor import IsInstructor
from exams.models.student_answers import StudentAnswer
from exams.serializers.student_answers import StudentAnswerSerializer
from exams.filters.student_answers import StudentAnswersFilter


class StudentAnswersListCreate(ListCreateAPIView):

    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentAnswersFilter

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


class StudentAnswersRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer

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
