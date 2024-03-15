from rest_framework import serializers
from accounts.models import Instructor
from exams.models import Exam
from levels.models import Course

class ExamSerializer(serializers.ModelSerializer):

    instructor = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all())
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    url = serializers.HyperlinkedIdentityField(
        view_name="api:exams:ExamRetrieveUpdateDestroy",
        lookup_field="pk",
    )

    class Meta:
        model = Exam
        fields = ['url', 'id', 'title', 'instructor', 'start_date', 'end_date', 'course', 'exam_score',]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "PUT":
            NOT_REQUIRED_FILEDS = (
                "title",
                "instructor",
                "start_date",
                "end_date",
                "course",
                "exam_score"
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
        representation["course"] = {
            "id": instance.course.id,
            "title": instance.course.title,
        }
        return representation
