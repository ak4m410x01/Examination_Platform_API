from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from accounts.serializers.instructor import InstructorSerializer
from accounts.models.instructor import Instructor


class InstructorListCreate(ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
