"""
This module contains the views for handling CRUD operations on Level objects.

Classes:
- LevelListCreate: Handles the listing and creation of Level objects.
- LevelRetrieveUpdateDestroy: Handles the retrieval, updating, and deletion of Level objects.
"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from levels.serializers.levels import LevelSerializer
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isOwner import IsOwner
from levels.models.levels import Level


class LevelListCreate(ListCreateAPIView):
    """
    A view class that handles the listing and creation of Level objects.

    Attributes:
    - queryset: The queryset of Level objects to be used for listing.
    - serializer_class: The serializer class to be used for Level objects.
    """

    queryset = Level.objects.all()
    serializer_class = LevelSerializer

    def get_permissions(self):
        """
        Returns the list of permissions required for each HTTP method.

        Returns:
        - permission_classes: The list of permission classes required for the HTTP method.
        """

        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()


class LevelRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    A view class that handles the retrieval, updating, and deletion of Level objects.

    Attributes:
    - queryset: The queryset of Level objects to be used for retrieval, updating, and deletion.
    - serializer_class: The serializer class to be used for Level objects.
    """

    queryset = Level.objects.all()
    serializer_class = LevelSerializer

    def get_permissions(self):
        """
        Returns the list of permissions required for each HTTP method.

        Returns:
        - permission_classes: The list of permission classes required for the HTTP method.
        """

        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()
