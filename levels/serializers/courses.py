from rest_framework import serializers
from levels.models import Course
from accounts.models.instructor import Instructor
from accounts.models.student import Student


class CourseSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:levels:CourseRetrieveUpdateDestroy",
        lookup_field="pk"
    )

    class Meta:
        model = Course
        ordering = (id,)
        fields = ['url', 'id', 'course_code', 'title', 'description', 'duration', 'level', 'instructor', 'students']

    def validate_instructor(self, value):
        if not Instructor.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("The specified instructor does not exist")
        return value

    def validate_students(self, value):
        for student in value:
            if not Student.objects.filter(id=student.id).exists():
                raise serializers.ValidationError(f"The student with id {student.id} does not exist")
        return value
