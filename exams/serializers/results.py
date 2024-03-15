from rest_framework import serializers
from exams.models import Result, Exam, Question
from accounts.models import Student

class ResultSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="api:exams:ResultRetrieveUpdateDestroy",
        lookup_field="pk"
    )

    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())

    class Meta:
        model = Result
        ordering = (id,)
        fields = ['url', 'id', 'student', 'exam', 'score', 'date_taken',]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "PUT":
            NOT_REQUIRED_FILEDS = (
                "student",
                "exam",
                "score",
                "date_taken",
            )
            for field_name in NOT_REQUIRED_FILEDS:
                fields[field_name].required = False
        return fields

    def validate_score(self, score):
        if score > 100:
            raise serializers.ValidationError("Score cannot be greater than 100")
        return score

    def update(self, instance, validated_data):
        if 'score' in validated_data:
            raise serializers.ValidationError("The score cannot be updated after the exam is taken")
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["student"] = {
            "id": instance.student.id,
            "username": instance.student.username,
            "first_name": instance.student.first_name,
            "second_name": instance.student.second_name,
        }
        representation["exam"] = {
            "id": instance.exam.id,
            "title": instance.exam.title,
            "exam_score": instance.exam.exam_score,
        }
        return representation
