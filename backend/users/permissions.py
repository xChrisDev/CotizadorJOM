from rest_framework.permissions import BasePermission


class IsRoleAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        return hasattr(request.user, "profile") and request.user.profile.rol == "ADMIN"
