from django.urls import path, include

from exams.urls.results import urlpatterns as results_urls
from exams.urls.questions import urlpatterns as questions_urls
from exams.urls.exams import urlpatterns as exams_urls
from exams.urls.choices import urlpatterns as choices_urls
from exams.urls.student_answers import urlpatterns as student_choice

app_name = "levels"

urlpatterns = [
    path("", include(exams_urls)),
    path("results/", include(results_urls)),
    path("questions/", include(questions_urls)),
    path("choices/", include(choices_urls)),
    path("answers/", include(student_choice))
]
