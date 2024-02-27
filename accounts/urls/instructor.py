from django.urls import path
from accounts.views.instructor import (
    InstructorListCreate,
    InstructorRetrieveUpdateDestroy,
)

urlpatterns = [
    path("", InstructorListCreate.as_view(), name="InstructorListCreate"),
    path(
        "<int:pk>/",
        InstructorRetrieveUpdateDestroy.as_view(),
        name="InstructorRetrieveUpdateDestroy",
    ),
]
