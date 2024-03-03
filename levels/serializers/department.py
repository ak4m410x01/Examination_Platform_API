from rest_framework import serializers
from levels.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:levels:DepartmentRetrieveUpdateDestroy",
        lookup_field="pk"
    )

    class Meta:
        model = Department
        ordering = (id,)
        fields = ['url', 'id', 'title']
