from django.urls import path
from exams.views.results import ResultListCreate, ResultRetrieveUpdateDestroy

urlpatterns = [
    path("", ResultListCreate.as_view(), name="ResultListCreate"),
    path(
        "<int:pk>/",
        ResultRetrieveUpdateDestroy.as_view(),
        name="ResultRetrieveUpdateDestroy",
    ),
]
