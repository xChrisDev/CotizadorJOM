from rest_framework import serializers
from django.contrib.auth.models import User
from phonenumber_field.serializerfields import PhoneNumberField
from .models import Admin, Seller, PurchasingStaff, Customer, UserProfile


class BaseUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)  

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", None)
        if user_data:
            BaseUserSerializer().update(instance.profile.user, user_data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["rol", "status"]
        read_only_fields = [
            "rol",
            "status",
        ]


class AdminSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(source="profile.user")
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = Admin
        fields = ["id", "user", "profile"]

    def create(self, validated_data):
        user_data = validated_data.pop("profile")["user"]
        user = BaseUserSerializer().create(user_data)
        profile = UserProfile.objects.create(user=user, rol="ADMIN", status="ACTIVE")
        return Admin.objects.create(profile=profile)

    def update(self, instance, validated_data):
        user_data = validated_data.get("profile", {}).get("user", {})
        if user_data:
            BaseUserSerializer().update(instance.profile.user, user_data)
        return instance


class SellerSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(source="profile.user")
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = Seller
        fields = ["id", "user", "profile", "workstation"]

    def create(self, validated_data):
        user_data = validated_data.pop("profile")["user"]
        workstation = validated_data.get("workstation", "")
        user = BaseUserSerializer().create(user_data)
        profile = UserProfile.objects.create(user=user, rol="SELLER", status="ACTIVE")
        return Seller.objects.create(profile=profile, workstation=workstation)

    def update(self, instance, validated_data):
        user_data = validated_data.get("profile", {}).get("user", {})
        if user_data:
            BaseUserSerializer().update(instance.profile.user, user_data)
        instance.workstation = validated_data.get("workstation", instance.workstation)
        instance.save()
        return instance


class PurchasingStaffSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(source="profile.user")
    profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = PurchasingStaff
        fields = ["id", "user", "profile"]

    def create(self, validated_data):
        user_data = validated_data.pop("profile")["user"]
        user = BaseUserSerializer().create(user_data)
        profile = UserProfile.objects.create(user=user, rol="STAFF", status="ACTIVE")
        return PurchasingStaff.objects.create(profile=profile)

    def update(self, instance, validated_data):
        user_data = validated_data.get("profile", {}).get("user", {})
        if user_data:
            BaseUserSerializer().update(instance.profile.user, user_data)
        return instance


class CustomerSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer(source="profile.user")
    profile = UserProfileSerializer(read_only=True)
    phone_number = PhoneNumberField(required=True)
    customer_type = serializers.ChoiceField(
        choices=[("A", "A"), ("B", "B"), ("C", "C")]
    )

    class Meta:
        model = Customer
        fields = ["id", "user", "profile", "customer_type", "phone_number"]

    def validate(self, data):
        if not data.get("phone_number"):
            raise serializers.ValidationError(
                "Los clientes deben tener número de teléfono."
            )
        if not data.get("customer_type"):
            raise serializers.ValidationError("Se debe especificar el tipo de cliente.")
        return data

    def create(self, validated_data):
        user_data = validated_data.pop("profile")["user"]
        phone_number = validated_data.get("phone_number")
        customer_type = validated_data.get("customer_type")

        # Crear usuario
        user = BaseUserSerializer().create(user_data)

        # Crear perfil
        profile = UserProfile.objects.create(
            user=user, rol="CUSTOMER", status="PENDING"
        )

        # Crear cliente
        return Customer.objects.create(
            profile=profile, phone_number=phone_number, customer_type=customer_type
        )

    def update(self, instance, validated_data):
        user_data = validated_data.get("profile", {}).get("user", {})
        if user_data:
            BaseUserSerializer().update(instance.profile.user, user_data)

        instance.phone_number = validated_data.get(
            "phone_number", instance.phone_number
        )
        instance.customer_type = validated_data.get(
            "customer_type", instance.customer_type
        )
        instance.save()
        return instance
