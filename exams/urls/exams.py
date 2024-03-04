from django.urls import path
from exams.views.exams import ExamListCreate, ExamRetrieveUpdateDestroy

urlpatterns = [
    path("", ExamListCreate.as_view(), name="ExamListCreate"),
    path(
        "<int:pk>/",
        ExamRetrieveUpdateDestroy.as_view(),
        name="ExamRetrieveUpdateDestroy",
    ),
]
