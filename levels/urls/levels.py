from django.urls import path
from levels.views.levels import LevelListCreate, LevelRetrieveUpdateDestroy

urlpatterns = [
    path("", LevelListCreate.as_view(), name="LevelListCreate"),
    path(
        "<int:pk>/",
        LevelRetrieveUpdateDestroy.as_view(),
        name="LevelRetrieveUpdateDestroy",
    ),
]
