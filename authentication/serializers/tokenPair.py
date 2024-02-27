from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


def get_user_role(user_type: int) -> str | None:
    if user_type == 1:
        return "admin"
    elif user_type == 2:
        return "instructor"
    elif user_type == 3:
        return "student"
    return None


class TokenPairSerializer(TokenObtainPairSerializer):
    user_id = serializers.IntegerField(read_only=True)
    user_role = serializers.CharField(read_only=True)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_role"] = get_user_role(user.user_type)
        return token
