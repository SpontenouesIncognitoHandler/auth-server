from rest_framework import serializers
from .models import User,Organization

class OrgSerializer(serializers.PrimaryKeyRelatedField):
    class Meta:
        model = Organization
        fields = '__all__'
    def to_internal_value(self, data):
        try:
            return Organization.objects.get(org_id=data)
        except Organization.DoesNotExist:
            raise serializers.ValidationError("No organization found with the given ID.")
    

class UserSerializer(serializers.ModelSerializer):
    organization = OrgSerializer(queryset=Organization.objects.all())

    class Meta:
        model = User
        fields = ['name', 'role', 'user_token', 'organization']

class OrgTokenSerializer(serializers.Serializer):
    org_id = serializers.CharField(max_length=36)
    token = serializers.CharField()