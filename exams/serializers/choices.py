from rest_framework import serializers
from exams.models import Choice
from exams.models import Question

class ChoiceSerializer(serializers.ModelSerializer):

    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())

    class Meta:
        model = Choice
        fields = ['id', 'question', 'text', 'is_correct']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "PUT":
            NOT_REQUIRED_FILEDS = (
                "question",
                "text",
                "is_correct",
            )
            for field_name in NOT_REQUIRED_FILEDS:
                fields[field_name].required = False
        return fields

    def validate_text(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("The text should not be more than 200 characters")
        if not value.strip():
            raise serializers.ValidationError("The text cannot be empty")
        return value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["question"] = {
            "id": instance.question.id,
            "text": instance.question.text
        }
        return representation
