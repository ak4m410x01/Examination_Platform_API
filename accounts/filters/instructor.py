import django_filters
from accounts.models.instructor import Instructor


class InstructorFilter(django_filters.FilterSet):
    username = django_filters.CharFilter("username", lookup_expr="icontains")
    email = django_filters.CharFilter("email", lookup_expr="icontains")

    first_name = django_filters.CharFilter("first_name", lookup_expr="icontains")
    last_name = django_filters.CharFilter("last_name", lookup_expr="icontains")

    gender = django_filters.CharFilter("gender", lookup_expr="icontains")
    birth_date = django_filters.CharFilter("birth_date", lookup_expr="icontains")

    city = django_filters.CharFilter("city", lookup_expr="icontains")
    address = django_filters.CharFilter("address", lookup_expr="icontains")

    specialized_in = django_filters.CharFilter(
        "specialized_in", lookup_expr="icontains"
    )

    class Meta:
        model = Instructor
        fields = [
            "username",
            "email",
            "first_name",
            "second_name",
            "gender",
            "birth_date",
            "city",
            "address",
            "specialized_in",
        ]
