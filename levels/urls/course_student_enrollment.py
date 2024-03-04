from django.urls import path
from levels.views.course_student_enrollment import CourseStudentEnrollmentListCreate, CourseStudentEnrollmentRetrieveUpdateDestroy

urlpatterns = [
    path("", CourseStudentEnrollmentListCreate.as_view(), name="CourseStudentEnrollmentListCreate"),
    path(
        "<int:pk>/",
        CourseStudentEnrollmentRetrieveUpdateDestroy.as_view(),
        name="CourseStudentEnrollmentRetrieveUpdateDestroy",
    ),
]
