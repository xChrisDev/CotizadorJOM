from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrOwner(BasePermission):
    """
    - Admin puede ver/editar/eliminar todo.
    - Cualquiera puede crear usuarios con rol CUSTOMER.
    - Usuarios normales solo pueden ver o editar su propio perfil.
    """

    def has_permission(self, request, view):
        user = request.user
        method = request.method

        # Permitir crear clientes libremente (registro público)
        if method == "POST":
            rol = (
                request.data.get("profile", {}).get("rol", "")
                or request.data.get("rol", "")
            ).upper()
            if rol in ["", "CUSTOMER"]:
                return True

        # Si no está autenticado, no puede hacer nada más
        if not user or not user.is_authenticated:
            return False

        # Permitir si es admin
        if hasattr(user, "profile") and user.profile.rol.upper() == "ADMIN":
            return True

        # Permitir lectura de su propio perfil (control en object level)
        return method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Admin puede ver/modificar todo
        if hasattr(user, "profile") and user.profile.rol.upper() == "ADMIN":
            return True

        # Si el objeto tiene relación a un usuario, permitir solo si es el mismo
        owner_id = getattr(obj.profile.user, "id", None)
        return owner_id == user.id
