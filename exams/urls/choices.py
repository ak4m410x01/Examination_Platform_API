from django.urls import path
from exams.views.choices import ChoiceListCreate, ChoiceRetrieveUpdateDestroy

urlpatterns = [
    path("", ChoiceListCreate.as_view(), name="ChoiceListCreate"),
    path(
        "<int:pk>/",
        ChoiceRetrieveUpdateDestroy.as_view(),
        name="ChoiceRetrieveUpdateDestroy",
    ),
]
