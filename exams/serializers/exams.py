from rest_framework import serializers
from accounts.models import Instructor
from exams.models import Exam
from levels.models import Course
from pytz import timezone as pytz_timezone

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
        # Convert start_date and end_date to Cairo timezone
        start_date_utc = instance.start_date
        end_date_utc = instance.end_date
        cairo_tz = pytz_timezone('Africa/Cairo')
        start_date_tz = start_date_utc.astimezone(cairo_tz)
        end_date_tz = end_date_utc.astimezone(cairo_tz)
        representation["start_date"] = start_date_tz.isoformat()
        representation["end_date"] = end_date_tz.isoformat()

        return representation

    def create(self, validated_data):
        # Convert start_date and end_date to Cairo timezone before saving
        cairo_tz = pytz_timezone('Africa/Cairo')
        if 'start_date' in validated_data:
            start_date_utc = validated_data['start_date']
            start_date_tz = start_date_utc.astimezone(cairo_tz)
            validated_data['start_date'] = start_date_tz
        if 'end_date' in validated_data:
            end_date_utc = validated_data['end_date']
            end_date_tz = end_date_utc.astimezone(cairo_tz)
            validated_data['end_date'] = end_date_tz
        return super().create(validated_data)
