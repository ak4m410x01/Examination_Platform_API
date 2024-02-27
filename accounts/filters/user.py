import django_filters
from accounts.models.user import User


class UserFilter(django_filters.FilterSet):
    role = django_filters.CharFilter(lookup_expr="icontains")

    username = django_filters.CharFilter("username", lookup_expr="icontains")
    email = django_filters.CharFilter("email", lookup_expr="icontains")

    first_name = django_filters.CharFilter("first_name", lookup_expr="icontains")
    last_name = django_filters.CharFilter("last_name", lookup_expr="icontains")

    class Meta:
        model = User
        fields = [
            "role",
            "username",
            "email",
            "first_name",
            "second_name",
        ]
