from rest_framework import serializers
from exams.models import Exam
from accounts.models.instructor import Instructor
from levels.models.courses import Course

class ExamSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:exams:ExamRetrieveUpdateDestroy",
        lookup_field="pk",
    )

    class Meta:
        model = Exam
        fields = ['url', 'id', 'title', 'instructor', 'start_date', 'end_date', 'course']

    def validate_instructor(self, value):
        if not Instructor.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("The specified instructor does not exist")
        return value

    def validate_course(self, value):
        if not Course.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("The specified course does not exist")
        return value
