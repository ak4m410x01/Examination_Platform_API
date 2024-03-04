from django.urls import path, include

from exams.urls.results import urlpatterns as results_urls
from exams.urls.questions import urlpatterns as questions_urls
from exams.urls.exams import urlpatterns as exams_urls
from exams.urls.choices import urlpatterns as choices_urls

app_name = "levels"

urlpatterns = [
    path("results/", include(results_urls)),
    path("questions/", include(questions_urls)),
    path("exams/", include(exams_urls)),
    path("choices/", include(choices_urls)),
]
