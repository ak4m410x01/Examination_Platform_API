from django.urls import path
from exams.views.questions import QuestionListCreate, QuestionRetrieveUpdateDestroy

urlpatterns = [
    path("", QuestionListCreate.as_view(), name="QuestionListCreate"),
    path(
        "<int:pk>/",
        QuestionRetrieveUpdateDestroy.as_view(),
        name="QuestionRetrieveUpdateDestroy",
    ),
]
