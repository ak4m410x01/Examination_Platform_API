from rest_framework import serializers
from exams.models import StudentAnswer
from accounts.models import Student
from exams.models import Exam, Question, Choice


class StudentAnswerSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="api:exams:StudentAnswersRetrieveUpdateDestroy",
        lookup_field="pk"
    )

    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    student_choice = serializers.PrimaryKeyRelatedField(queryset=Choice.objects.all())

    class Meta:
        model = StudentAnswer
        ordering = (id,)
        fields = ['url', 'id', 'student', 'exam', 'question', 'student_choice',]

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "PUT":
            NOT_REQUIRED_FILEDS = (
                "student",
                "exam",
                "question",
                "student_choice",
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
        representation["exam"] = {
            "id": instance.exam.id,
            "title": instance.exam.title,
        }
        representation["question"] = {
            "id": instance.question.id,
            "text": instance.question.text,
            "choices": [
                {
                    "id": choice.id,
                    "choice": choice.text,
                    "is_correct": choice.is_correct
                }
                for choice in instance.question.choices.all()
            ],
        }
        representation["student_choice"] = {
            "id": instance.student_choice.id,
            "choice": instance.student_choice.text,
            "is_correct": instance.student_choice.is_correct
        }
        return representation
