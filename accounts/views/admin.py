from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend

from accounts.serializers.admin import AdminSerializer
from accounts.filters.admin import AdminFilter
from accounts.models.admin import Admin


class AdminListCreate(ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdminFilter


class AdminRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
