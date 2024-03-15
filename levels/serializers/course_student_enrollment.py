from rest_framework import serializers
from levels.models import CourseStudentEnrollment
from accounts.models import Student
from levels.models import Course

class CourseStudentEnrollmentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:levels:CourseStudentEnrollmentRetrieveUpdateDestroy",
        lookup_field="pk"
    )

    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = CourseStudentEnrollment
        ordering = (id,)
        fields = ['url', 'id', 'student', 'course', 'pass_status']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "PUT":
            NOT_REQUIRED_FILEDS = (
                "student",
                "course",
                "pass_status",
            )
            for field_name in NOT_REQUIRED_FILEDS:
                fields[field_name].required = False
        return fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["student"] = {
            "id": instance.student.id,
            "username": instance.student.username,
            "first_name": instance.student.first_name,
            "second_name": instance.student.second_name,
        }
        representation["course"] = {
            "id": instance.course.id,
            "title": instance.course.title,
        }
        return representation
