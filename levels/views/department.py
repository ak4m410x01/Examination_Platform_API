"""
This module contains the views for handling Department-related operations in the Examination Platform API.

Classes:
- DepartmentListCreate: Handles the listing and creation of Department objects.
- DepartmentRetrieveUpdateDestroy: Handles the retrieval, update, and deletion of Department objects.
"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from levels.serializers.department import DepartmentSerializer
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isOwner import IsOwner
from levels.models.department import Department


class DepartmentListCreate(ListCreateAPIView):
    """
    A view class that handles the listing and creation of Department objects.

    Attributes:
    - queryset: The queryset of Department objects to be used for listing.
    - serializer_class: The serializer class to be used for Department objects.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        """
        Returns the list of permissions required for the view based on the request method.

        Returns:
        - A list of permission classes.
        """
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()


class DepartmentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    A view class that handles the retrieval, update, and deletion of Department objects.

    Attributes:
    - queryset: The queryset of Department objects to be used for retrieval, update, and deletion.
    - serializer_class: The serializer class to be used for Department objects.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        """
        Returns the list of permissions required for the view based on the request method.

        Returns:
        - A list of permission classes.
        """
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()
