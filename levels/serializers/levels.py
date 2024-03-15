from rest_framework import serializers
from levels.models import Level


class LevelSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:levels:LevelRetrieveUpdateDestroy",
        lookup_field="pk"
    )

    class Meta:
        model = Level
        ordering = (id,)
        fields = ['url', 'level_number']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        if request and request.method == "PUT":
            NOT_REQUIRED_FILEDS = (
                "level_number",
            )
            for field_name in NOT_REQUIRED_FILEDS:
                fields[field_name].required = False
        return fields
