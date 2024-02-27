from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers.tokenPair import TokenPairSerializer


class TokenObtainPair(TokenObtainPairView):
    serializer_class = TokenPairSerializer
