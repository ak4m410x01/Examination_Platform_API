from django.urls import path
from accounts.views.student import StudentListCreate, StudentRetrieveUpdateDestroy

urlpatterns = [
    path("", StudentListCreate.as_view(), name="StudentListCreate"),
    path(
        "<int:pk>/",
        StudentRetrieveUpdateDestroy.as_view(),
        name="StudentRetrieveUpdateDestroy",
    ),
]
