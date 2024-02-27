from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from accounts.serializers.instructor import InstructorSerializer
from accounts.filters.instructor import InstructorFilter
from accounts.models.instructor import Instructor


class InstructorListCreate(ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = InstructorFilter


class InstructorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
