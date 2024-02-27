from django.urls import path, include

from authentication.urls.token import urlpatterns as token_urls

app_name = "authentication"

urlpatterns = [
    path("token/", include(token_urls), name="token"),
]
