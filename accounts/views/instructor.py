from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from accounts.serializers.instructor import InstructorSerializer
from accounts.filters.instructor import InstructorFilter
from accounts.models.instructor import Instructor
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isOwner import IsOwner


class InstructorListCreate(ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = InstructorFilter

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()


class InstructorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()
