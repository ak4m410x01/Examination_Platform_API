from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from authentication.views.tokenPair import TokenObtainPair

urlpatterns = [
    path("", TokenObtainPair.as_view(), name="TokenObtainPair"),
    path("refresh/", TokenRefreshView.as_view(), name="TokenRefreshView"),
    path("verify/", TokenVerifyView.as_view(), name="TokenVerifyView"),
]
