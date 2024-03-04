from rest_framework import serializers
from levels.models import CourseStudentEnrollment
from accounts.models.student import Student
from levels.models.courses import Course

class CourseStudentEnrollmentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:levels:CourseStudentEnrollmentRetrieveUpdateDestroy",
        lookup_field="pk"
    )
    class Meta:
        model = CourseStudentEnrollment
        ordering = (id,)
        fields = ['url', 'id', 'student', 'course', 'pass_status']

    def validate_student(self, value):
        if not Student.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("The specified student does not exist")
        return value

    def validate_course(self, value):
        if not Course.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("The specified course does not exist")
        return value
