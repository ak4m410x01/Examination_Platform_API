from django.urls import path, include


from levels.urls.levels import urlpatterns as level_urls
from levels.urls.department import urlpatterns as department_urls
from levels.urls.courses import urlpatterns as courses_urls
from levels.urls.course_student_enrollment import urlpatterns as course_student_enrollment_urls

app_name = "levels"

urlpatterns = [
    path("levels/", include(level_urls)),
    path("departments/", include(department_urls)),
    path("courses/", include(courses_urls)),
    path("enrollments/", include(course_student_enrollment_urls)),
]
