from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    """
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'username', 'email', 'avatar_url', 'title', 'bio', 'phone_number', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
