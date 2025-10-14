from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import check_password
from .models import User, Token
from .serializers import UserSerializer
from .permissions import IsAuth
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import UserFilter
from .pagination import PageNumberPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuth]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = UserFilter
    search_fields = ["username", "first_name", "last_name"]
    ordering_fields = ["username", "first_name", "last_name", "status"]
    pagination_class = PageNumberPagination

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return super().get_permissions()

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username y contraseña son requeridos."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND
            )

        if user.status == "PENDING":
            return Response(
                {"error": "Su solicitud aun no ha sido aceptada"},
                status=status.HTTP_403_FORBIDDEN,
            )

        if user.status == "BANNED":
            return Response(
                {"error": "Usuario suspendido."}, status=status.HTTP_403_FORBIDDEN
            )

        if user.status == "REJECTED":
            return Response(
                {"error": "Usuario rechazado."}, status=status.HTTP_403_FORBIDDEN
            )

        if not check_password(password, user.password):
            return Response(
                {"error": "Contraseña incorrecta."}, status=status.HTTP_401_UNAUTHORIZED
            )

        token = Token.generate_token(user)

        return Response(
            {
                "token": token.key,
                "user": UserSerializer(user).data,
            },
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["post"])
    def logout(self, request):
        if hasattr(request, "auth") and request.auth:
            request.auth.delete()
            return Response(
                {"message": "Sesión cerrada correctamente."}, status=status.HTTP_200_OK
            )
        return Response(
            {"error": "No hay token activo o sesión iniciada."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=False, methods=["get"])
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if "role" not in request.data:
                print("⚠️ No hay role en el request")
                serializer.validated_data["role"] = "CUSTOMER"
            if "status" not in request.data:
                print("⚠️ No hay status en el request")
                serializer.validated_data["status"] = "PENDING"

            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"], url_path="get_by_role/(?P<role>[^/.]+)")
    def get_by_role(self, request, role=None):
        users = self.queryset.filter(role=role.upper())
        filtered_users = UserFilter(request.GET, queryset=users).qs

        if not filtered_users.exists():
            return Response(
                {"error": f"No se encontraron usuarios con el rol '{role}'."},
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.paginate_queryset(filtered_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="pending")
    def get_pending_users(self, request):
        users = self.queryset.filter(role="CUSTOMER", status="PENDING")

        filtered_users = UserFilter(request.GET, queryset=users).qs

        if not filtered_users.exists():
            return Response(
                {"error": "No hay usuarios pendientes de aceptación."},
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.paginate_queryset(filtered_users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
