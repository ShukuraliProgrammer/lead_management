from rest_framework import permissions
from django.contrib.auth import get_user_model

User = get_user_model()


class IsAttorney(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == User.UserRole.ATTORNEY:
            return True
        return False
