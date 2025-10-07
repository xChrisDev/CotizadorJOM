from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    """Perfil base para todos los usuarios"""

    STATUS_CHOICES = [
        ("PENDING", "Pendiente"),
        ("ACTIVE", "Activo"),
        ("BANNED", "Suspendido"),
        ("REJECTED", "Rechazado"),
    ]

    ROL_CHOICES = [
        ("SELLER", "Vendedor"),
        ("PURCHASING", "Compras"),
        ("CLIENT", "Cliente"),
        ("ADMIN", "Administrador"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = PhoneNumberField(blank=True, null=True)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"

    def __str__(self):
        return f"{self.user.username} - {self.get_rol_display()}"


class Seller(models.Model):
    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="seller_data",
        null=True,
        blank=True,
    )
    workstation = models.CharField(max_length=100, verbose_name="Estación de trabajo")

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return f"{self.profile.user.get_full_name()} - {self.workstation}"


class PurchasingStaff(models.Model):
    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="purchasing_data",
        null=True,
        blank=True,
    )
    department = models.CharField(max_length=100, verbose_name="Departamento")

    class Meta:
        verbose_name = "Personal de Compras"
        verbose_name_plural = "Personal de Compras"

    def __str__(self):
        return f"{self.profile.user.get_full_name()} - {self.department}"


class Admin(models.Model):
    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="admin_data",
        null=True,
        blank=True,
    )
    full_access = models.BooleanField(default=True, verbose_name="Acceso completo")

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

    def __str__(self):
        return f"{self.profile.user.get_full_name()} - Admin"


class Client(models.Model):
    profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="client_data",
        null=True,
        blank=True,
    )
    STATUS_CHOICES = [
        ("A", "Tipo A"),
        ("B", "Tipo B"),
        ("C", "Tipo C"),
    ]
    client_type = models.CharField(max_length=20, choices=STATUS_CHOICES, default="A")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.profile.user.get_full_name()} - {self.client_type}"
