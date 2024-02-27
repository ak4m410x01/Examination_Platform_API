from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from accounts.serializers.student import StudentSerializer
from accounts.filters.student import StudentFilter
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isOwner import IsOwner
from accounts.models.student import Student


class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentFilter

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()


class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()
