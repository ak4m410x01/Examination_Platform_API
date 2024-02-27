from django.contrib.auth.hashers import make_password
from re import match
from datetime import datetime, date
from rest_framework import serializers
from accounts.models.instructor import Instructor


class BaseInstructorSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:accounts:InstructorRetrieveUpdateDestroy",
        lookup_field="pk",
    )

    class Meta:
        model = Instructor
        ordering = (id,)
        fields = [
            "url",
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "second_name",
            "third_name",
            "fourth_name",
            "last_name",
            "gender",
            "birth_date",
            "city",
            "address",
            "phone",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
            "user_type",
            "specialized_in",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "date_joined": {"read_only": True},
        }

    def validate_username(self, value: str) -> str:
        qs = Instructor.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} already used. try another one!")

        regex = r"^[a-zA-Z_][A-Za-z0-9_\.]+$"
        if not match(regex, value):
            raise serializers.ValidationError("Invalid username :(")

        return value

    def validate_email(self, value: str) -> str:
        qs = Instructor.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} already used. try another one!")
        return value

    def validate_gender(self, value: str) -> str:
        regex = r"^[mf]$"
        if not match(regex, value):
            raise serializers.ValidationError(f"gender must be 'm' or 'f'.")
        return value

    def validate_birth_date(self, value: str) -> str:
        if isinstance(value, date):
            value = value.strftime("%Y-%m-%d")

        try:
            dob = datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise serializers.ValidationError(
                "Date of birth must be in the format YYYY-MM-DD."
            )

        if dob.date() > datetime.now().date():
            raise serializers.ValidationError("Date of birth cannot be in the future.")

        return value

    def validate_phone(self, value: str) -> str:
        regex = r"^\+201[0125]\d{8}$"
        if not match(regex, value):
            raise serializers.ValidationError(
                "Egyptian phone number must be like: '+201234567890'"
            )

        return value


class InstructorSerializer(BaseInstructorSerializer):
    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "PUT":
            fields["user_type"].read_only = True
            NOT_REQUIRED_FILEDS = (
                "username",
                "email",
                "password",
                "first_name",
                "second_name",
                "gender",
                "birth_date",
                "specialized_in",
            )
            for field_name in NOT_REQUIRED_FILEDS:
                fields[field_name].required = False
        return fields
    
    def create(self, validated_data):
        # Hash the password before creating the admin instance
        password = validated_data.pop("password", None)
        if password:
            validated_data["password"] = make_password(password)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Hash the password before updating the admin instance
        password = validated_data.pop("password", None)
        if password:
            validated_data["password"] = make_password(password)
        return super().update(instance, validated_data)
