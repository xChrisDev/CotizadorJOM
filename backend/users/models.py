from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

ROLES = (
    ("ADMIN", "Admin"),
    ("SELLER", "Vendedor"),
    ("CUSTOMER", "Cliente"),
    ("STAFF", "Staff"),
)

STATUS = (
    ("ACTIVE", "Activo"),
    ("BANNED", "Baneado"),
    ("REJECTED", "Rechazado"),
    ("PENDING", "Pendiente"),
)

CUSTOMER_TYPE = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    rol = models.CharField(max_length=20, choices=ROLES)
    status = models.CharField(max_length=20, choices=STATUS)

    class Meta:
        db_table = "profile_info"


class Seller(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    workstation = models.CharField(max_length=100)

    class Meta:
        db_table = "sellers"


class PurchasingStaff(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = "purchasing_staff"


class Admin(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = "admins"


class Customer(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPE, default="A")
    phone_number = PhoneNumberField()

    class Meta:
        db_table = "customers"
