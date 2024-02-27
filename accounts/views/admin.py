from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from accounts.serializers.admin import AdminSerializer
from accounts.models.admin import Admin


class AdminListCreate(ListCreateAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class AdminRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
