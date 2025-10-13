from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed
from .models import Token
from django.utils import timezone


class IsAuth(BasePermission):
    """
    Permiso personalizado que valida el token de autenticación.
    """
    def has_permission(self, request, view):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return False

        try:
            prefix, key = auth_header.split(" ")
            if prefix != "Token":
                return False
        except ValueError:
            return False

        try:
            token = Token.objects.select_related('user').get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Token inválido")

        # Verificar si el token ha expirado
        if token.expires < timezone.now():
            token.delete()  # Opcional: eliminar tokens expirados
            raise AuthenticationFailed("Token expirado")

        # Guardar el usuario y el token en el request para uso posterior
        request.user = token.user
        request.auth = token
        return True