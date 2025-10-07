from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, viewsets

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .permissions import IsRoleAdmin
from .models import Seller, PurchasingStaff, Admin, Client, UserProfile
from .serializers import (
    UserSerializer,
    SellerSerializer,
    PurchasingStaffSerializer,
    AdminSerializer,
    ClientSerializer,
    SellerCreateSerializer,
    PurchasingStaffCreateSerializer,
    AdminCreateSerializer,
    ClientCreateSerializer,
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    permission_classes = [IsRoleAdmin]

    def get_serializer_class(self):
        if self.action == 'create':
            return SellerCreateSerializer
        return SellerSerializer

    def create(self, request, *args, **kwargs):
        write_serializer = self.get_serializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        instance = write_serializer.save()
        read_serializer = SellerSerializer(instance)
        headers = self.get_success_headers(read_serializer.data)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PurchasingStaffViewSet(viewsets.ModelViewSet):
    queryset = PurchasingStaff.objects.all()
    permission_classes = [IsRoleAdmin]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return PurchasingStaffCreateSerializer
        return PurchasingStaffSerializer

    def create(self, request, *args, **kwargs):
        write_serializer = self.get_serializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        instance = write_serializer.save()
        read_serializer = PurchasingStaffSerializer(instance)
        headers = self.get_success_headers(read_serializer.data)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    permission_classes = [IsRoleAdmin]

    def get_serializer_class(self):
        if self.action == 'create':
            return AdminCreateSerializer
        return AdminSerializer

    def create(self, request, *args, **kwargs):
        write_serializer = self.get_serializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        instance = write_serializer.save()
        read_serializer = AdminSerializer(instance)
        headers = self.get_success_headers(read_serializer.data)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [AllowAny]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ClientCreateSerializer
        return ClientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client_instance = serializer.save()
        username = client_instance.profile.user.username
        Token.objects.create(user=client_instance.profile.user)
        response_data = {"success": "Nuestro equipo pronto revisará su solicitud."}
        return Response(response_data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = get_object_or_404(User, username=username)

    if not user.check_password(password):
        return Response(
            {"error": "Contraseña no válida"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        profile = user.profile
        if profile.status == "PENDING":
            return Response(
                {"error": "Aún no se ha aceptado tu solicitud."},
                status=status.HTTP_403_FORBIDDEN,
            )
        if profile.status == "BANNED":
            return Response(
                {"error": "Tu cuenta ha sido suspendida."},
                status=status.HTTP_403_FORBIDDEN,
            )
        if profile.status == "REJECTED":
            return Response(
                {"error": "Tu solicitud ha sido rechazada."},
                status=status.HTTP_403_FORBIDDEN,
            )
    except UserProfile.DoesNotExist:
        return Response(
            {"error": "El perfil de este usuario no existe."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    token, created = Token.objects.get_or_create(user=user)
    
    data = {"username": user.username, "rol": profile.rol}

    return Response({"token": token.key, "user": data}, status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def me(request):
    user = request.user
    try:
        profile = user.profile
        data = {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "rol": profile.get_rol_display(),
            "status": profile.get_status_display(),
            "phone_number": str(profile.phone_number),
        }
        return Response({"user": data}, status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
        return Response(
            {"error": "Perfil de usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND
        )