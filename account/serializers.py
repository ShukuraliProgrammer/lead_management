from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        max_length=150
    )
    password = serializers.CharField(required=True, write_only=True,
        style={'input_type': 'password'})