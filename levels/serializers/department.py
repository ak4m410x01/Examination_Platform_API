from rest_framework import serializers
from levels.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        ordering = (id,)
        fields = ['id', 'title']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "PUT":
            NOT_REQUIRED_FILEDS = (
                "title",
            )
            for field_name in NOT_REQUIRED_FILEDS:
                fields[field_name].required = False
        return fields
