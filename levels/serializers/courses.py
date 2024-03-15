from rest_framework import serializers
from levels.models import Course
from accounts.models import Instructor


class CourseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:levels:CourseRetrieveUpdateDestroy",
        lookup_field="pk"
    )

    instructor = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all())

    class Meta:
        model = Course
        ordering = (id,)
        fields = ['url', 'id', 'course_code', 'title', 'description', 'duration', 'level', 'instructor',]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "PUT":
            NOT_REQUIRED_FILEDS = (
                "course_code",
                "title",
                "description",
                "duration",
                "level",
                "instructor",
            )
            for field_name in NOT_REQUIRED_FILEDS:
                fields[field_name].required = False
        return fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["instructor"] = {
            "id": instance.instructor.id,
            "username": instance.instructor.username,
            "first_name": instance.instructor.first_name,
            "second_name": instance.instructor.second_name,
        }

        return representation
