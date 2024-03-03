from rest_framework import serializers
from exams.models import Question
from exams.models.exams import Exam

class QuestionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:exams:QuestionRetrieveUpdateDestroy",
        lookup_field="pk",
    )
    class Meta:
        model = Question
        fields = ['url', 'id', 'exam', 'text']

    def validate_exam(self, value):
        if not Exam.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("The specified exam does not exist")
        return value
