from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction
from .models import UserProfile, Seller, PurchasingStaff, Admin, Client
from phonenumber_field.serializerfields import PhoneNumberField

# ===================================================================
#  SERIALIZERS DE LECTURA
# ===================================================================


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserDataSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ["user", "phone_number", "rol", "status"]


class SellerSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = Seller
        fields = "__all__"


class PurchasingStaffSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = PurchasingStaff
        fields = "__all__"


class AdminSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = Admin
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = Client
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "profile",
        ]
        extra_kwargs = {"password": {"write_only": True}}


# ===================================================================
#  SERIALIZERS DE ESCRITURA
# ===================================================================


class BaseUserRoleSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True, default="")
    last_name = serializers.CharField(required=False, allow_blank=True, default="")
    email = serializers.EmailField(required=False, allow_blank=True, default="")
    phone_number = PhoneNumberField()

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("Este nombre de usuario ya está en uso.")
        return value

    def validate_email(self, value):
        if value and User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está en uso.")
        return value

    def create(
        self, validated_data, role, role_model, role_specific_data, status="PENDING"
    ):
        """
        Maneja la creación atómica de User, UserProfile y el modelo de rol.
        """
        with transaction.atomic():
            user = User.objects.create_user(
                username=validated_data["username"],
                password=validated_data["password"],
                first_name=validated_data.get("first_name", ""),
                last_name=validated_data.get("last_name", ""),
                email=validated_data.get("email", ""),
            )
            profile = UserProfile.objects.create(
                user=user,
                phone_number=validated_data["phone_number"],
                rol=role,
                status=status,
            )
            role_instance = role_model.objects.create(
                profile=profile, **role_specific_data
            )
        return role_instance


class SellerCreateSerializer(BaseUserRoleSerializer):
    workstation = serializers.CharField()

    def create(self, validated_data):
        role_specific_data = {"workstation": validated_data.pop("workstation")}
        return super().create(
            validated_data, "SELLER", Seller, role_specific_data, status="ACTIVE"
        )


class PurchasingStaffCreateSerializer(BaseUserRoleSerializer):
    department = serializers.CharField()

    def create(self, validated_data):
        role_specific_data = {"department": validated_data.pop("department")}
        return super().create(
            validated_data,
            "PURCHASING",
            PurchasingStaff,
            role_specific_data,
            status="ACTIVE",
        )


class AdminCreateSerializer(BaseUserRoleSerializer):
    full_access = serializers.BooleanField(default=True)

    def create(self, validated_data):
        role_specific_data = {"full_access": validated_data.pop("full_access", True)}
        return super().create(
            validated_data, "ADMIN", Admin, role_specific_data, status="ACTIVE"
        )


class ClientCreateSerializer(BaseUserRoleSerializer):
    client_type = serializers.ChoiceField(choices=Client.STATUS_CHOICES)

    def create(self, validated_data):
        role_specific_data = {"client_type": validated_data.pop("client_type")}
        return super().create(validated_data, "CLIENT", Client, role_specific_data)
