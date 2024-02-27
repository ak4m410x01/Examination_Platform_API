from rest_framework import serializers
from rest_framework.reverse import reverse
from accounts.models.user import User


class UserSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        ordering = (id,)
        fields = [
            "url",
            "role",
            "id",
            "username",
            "email",
            "first_name",
            "second_name",
        ]

    def get_role(self, obj):
        if obj.user_type == 1:
            return "admin"
        elif obj.user_type == 2:
            return "instructor"
        elif obj.user_type == 3:
            return "student"
        else:
            return None

    def get_url(self, obj):
        request = self.context.get("request")
        if not request:
            return None

        role = self.get_role(obj)
        view_name = ""

        if role == "admin":
            view_name = "accounts:AdminRetrieveUpdateDestroy"
        elif role == "instructor":
            view_name = "accounts:InstructorRetrieveUpdateDestroy"
        elif role == "student":
            view_name = "accounts:StudentRetrieveUpdateDestroy"
        else:
            return None

        return reverse(view_name, kwargs={"pk": obj.id}, request=request)
