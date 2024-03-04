"""
This module contains the views for managing choices in the examination platform API.

Classes:
- ChoiceListCreate: A view for listing and creating choices.
- ChoiceRetrieveUpdateDestroy: A view for retrieving, updating, and deleting choices.
"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from exams.serializers.choices import ChoiceSerializer
from exams.models.choices import Choice
from accounts.permissions.isAdmin import IsAdmin
from accounts.permissions.isOwner import IsOwner


class ChoiceListCreate(ListCreateAPIView):
    """
    A view for listing and creating choices.

    Attributes:
    - queryset: A queryset containing all the choices.
    - serializer_class: The serializer class used for serializing and deserializing choices.

    Methods:
    - get_permissions: Overrides the default method to set the appropriate permissions based on the request method.
    """

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def get_permissions(self):
        """
        Overrides the default method to set the appropriate permissions based on the request method.

        Returns:
        - A list of permission classes based on the request method.
        """
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "POST":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()


class ChoiceRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    """
    A view for retrieving, updating, and deleting choices.

    Attributes:
    - queryset: A queryset containing all the choices.
    - serializer_class: The serializer class used for serializing and deserializing choices.

    Methods:
    - get_permissions: Overrides the default method to set the appropriate permissions based on the request method.
    """

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def get_permissions(self):
        """
        Overrides the default method to set the appropriate permissions based on the request method.

        Returns:
        - A list of permission classes based on the request method.
        """
        if self.request.method == "GET":
            self.permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]
        elif self.request.method == "PUT":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        elif self.request.method == "DELETE":
            self.permission_classes = [IsAuthenticated & IsAdmin]
        return super().get_permissions()
