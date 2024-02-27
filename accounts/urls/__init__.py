from django.urls import path, include
from accounts.urls.admin import urlpatterns as admin_urls
from accounts.urls.instructor import urlpatterns as instructor_urls
from accounts.urls.student import urlpatterns as student_urls

app_name = "accounts"

urlpatterns = [
    path("admins/", include(admin_urls)),
    path("instructors/", include(instructor_urls)),
    path("students/", include(student_urls)),
]
