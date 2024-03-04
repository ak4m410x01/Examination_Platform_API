from django.urls import path
from levels.views.department import DepartmentListCreate, DepartmentRetrieveUpdateDestroy

urlpatterns = [
    path("", DepartmentListCreate.as_view(), name="DepartmentListCreate"),
    path(
        "<int:pk>/",
        DepartmentRetrieveUpdateDestroy.as_view(),
        name="DepartmentRetrieveUpdateDestroy",
    ),
]
