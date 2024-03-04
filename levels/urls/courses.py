from django.urls import path
from levels.views.courses import CourseListCreate, CourseRetrieveUpdateDestroy

urlpatterns = [
    path("", CourseListCreate.as_view(), name="CourseListCreate"),
    path(
        "<int:pk>/",
        CourseRetrieveUpdateDestroy.as_view(),
        name="CourseRetrieveUpdateDestroy",
    ),
]
