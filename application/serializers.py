from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import Application
from .utils import file_upload_validator

class ApplicationSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['first_name', 'last_name', 'email', 'resume']
        extra_kwargs = {
            'first_name': {'write_only': True, 'required': True},
            'email': {'write_only': True, 'required': True},
        }

    def validate(self, attrs):
        super().validate(attrs)
        file = attrs.get("resume")
        file_upload_validator(file)
        return attrs


class ApplicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"


class ApplicationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['status']

    def validate(self, attrs):
        if attrs['status'] != Application.ApplicationStatus.REACHED_OUT:
            raise serializers.ValidationError(_('This status is not supported'))
        return attrs