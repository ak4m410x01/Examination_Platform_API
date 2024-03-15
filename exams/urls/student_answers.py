from django.urls import path
from exams.views.student_answers import StudentAnswersListCreate, StudentAnswersRetrieveUpdateDestroy

urlpatterns = [
    path("", StudentAnswersListCreate.as_view(), name="StudentAnswersListCreate"),
    path(
        "<int:pk>/",
        StudentAnswersRetrieveUpdateDestroy.as_view(),
        name="StudentAnswersRetrieveUpdateDestroy",
    ),
]
