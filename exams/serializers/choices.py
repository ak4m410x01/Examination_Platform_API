from rest_framework import serializers
from exams.models import Choice
from exams.models.questions import Question

class ChoiceSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:exams:ChoiceRetrieveUpdateDestroy",
        lookup_field="pk",
    )

    class Meta:
        model = Choice
        fields = ['id', 'question', 'text', 'is_correct']

    def validate_question(self, value):
        if not Question.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("The specified question does not exist")
        return value

    def validate_text(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("The text should not be more than 200 characters")
        if not value.strip():
            raise serializers.ValidationError("The text cannot be empty")
        return value
