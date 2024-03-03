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
        fields = ['url', 'id', 'level_number', 'courses']
