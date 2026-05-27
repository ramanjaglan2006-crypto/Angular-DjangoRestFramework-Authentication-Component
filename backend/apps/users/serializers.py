from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.profiles.models import Profile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'created_at')
        read_only_fields = ('id', 'created_at')

class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a new user.
    """
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password_confirm')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        from .services import user_create
        validated_data.pop('password_confirm')
        return user_create(**validated_data)
