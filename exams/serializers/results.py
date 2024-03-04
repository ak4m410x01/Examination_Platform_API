from rest_framework import serializers
from exams.models import Result, Exam
from accounts.models import Student

class ResultSerializer(serializers.ModelSerializer):
	url = serializers.HyperlinkedIdentityField(
		view_name="api:exams:ResultRetrieveUpdateDestroy",
		lookup_field="pk"
	)

	class Meta:
		model = Result
		ordering = (id,)
		fields = ['url', 'id', 'student', 'exam', 'score', 'date_taken', 'duration']
		extra_kwargs = {'date_taken': {'read_only': True}, 'duration': {'read_only': True}}

	def validate_student(self, student):
		if not Student.objects.filter(id=student.id).exists():
			raise serializers.ValidationError("The specified student does not exist")
		return student

	def validate_exam(self, exam):
		if not Exam.objects.filter(id=exam.id).exists():
			raise serializers.ValidationError("The specified exam does not exist")
		return exam

	def validate_score(self, score):
		if score > 100:
			raise serializers.ValidationError("Score cannot be greater than 100")
		return score

	def update(self, instance, validated_data):
		if 'score' in validated_data and instance.score is not None:
			raise serializers.ValidationError("The score cannot be updated after the exam is taken")
		return super().update(instance, validated_data)
