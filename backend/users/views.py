from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Admin, Seller, PurchasingStaff, Customer, UserProfile
from .serializers import (
    AdminSerializer,
    SellerSerializer,
    PurchasingStaffSerializer,
    CustomerSerializer,
)
from .permissions import IsAdminOrOwner


class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAdminOrOwner]

    pagination_class = UserPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "profile__user__username",
        "profile__user__first_name",
        "profile__user__last_name",
        "profile__user__email",
    ]

    filterset_fields = ["profile__status"]

    ordering_fields = [
        "profile__user__username",
        "profile__user__first_name",
        "profile__user__last_name",
        "profile__status",
    ]
    ordering = ["profile__user__username"]


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [IsAdminOrOwner]

    pagination_class = UserPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "profile__user__username",
        "profile__user__first_name",
        "profile__user__last_name",
        "profile__user__email",
        "workstation",
    ]

    filterset_fields = ["profile__status"]

    ordering_fields = [
        "profile__user__username",
        "profile__user__first_name",
        "profile__user__last_name",
        "workstation",
        "profile__status",
    ]
    ordering = ["profile__user__username"]


class StaffViewSet(viewsets.ModelViewSet):
    queryset = PurchasingStaff.objects.all()
    serializer_class = PurchasingStaffSerializer
    permission_classes = [IsAdminOrOwner]

    pagination_class = UserPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "profile__user__username",
        "profile__user__first_name",
        "profile__user__last_name",
        "profile__user__email",
    ]

    filterset_fields = ["profile__status"]

    ordering_fields = [
        "profile__user__username",
        "profile__user__first_name",
        "profile__user__last_name",
        "profile__status",
    ]
    ordering = ["profile__user__username"]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminOrOwner]

    pagination_class = UserPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "profile__user__username",
        "profile__user__first_name",
        "profile__user__last_name",
        "profile__user__email",
        "phone_number",
        "profile__status",
    ]

    filterset_fields = ["profile__status"]

    ordering_fields = [
        "profile__user__username",
        "profile__user__first_name",
        "profile__user__last_name",
        "profile__status",
    ]
    ordering = ["profile__user__username"]



@api_view(["POST"])
@permission_classes([AllowAny])
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
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
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
    except UserProfile.DoesNotExist:
        return Response({"error": "Perfil de usuario no encontrado."},
                        status=status.HTTP_404_NOT_FOUND)

    # Número telefónico solo si es cliente
    phone_number = None
    if profile.rol == "CUSTOMER":
        try:
            customer = user.customer
            phone_number = str(customer.phone_number)
        except Customer.DoesNotExist:
            phone_number = None

    data = {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "rol": profile.get_rol_display(),
        "status": profile.get_status_display(),
        "phone_number": phone_number
    }
    return Response({"user": data}, status=status.HTTP_200_OK)