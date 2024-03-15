from rest_framework import serializers
from exams.models import Question, Exam


class QuestionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:exams:QuestionRetrieveUpdateDestroy",
        lookup_field="pk",
    )

    choices = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), many=True)
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())

    class Meta:
        model = Question
        fields = ['id', 'url', 'exam', 'text', 'choices']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "POST":
            fields.pop("choices", None)
        if request and request.method == "PUT":
            NOT_REQUIRED_FILEDS = (
                "exam",
                "text",
                "choices"
            )
            for field_name in NOT_REQUIRED_FILEDS:
                fields[field_name].required = False
        return fields

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["exam"] = {
            "id": instance.exam.id,
            "title": instance.exam.title
        }

        choices = instance.choices.all()
        representation["choices"] = []
        for choice in choices:
            representation["choices"].append({
                "id": choice.id,
                "text": choice.text
            })
        return representation
