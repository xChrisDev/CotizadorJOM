import secrets
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .enums import ROLE_CHOICES, STATUS_CHOICES
from django.utils import timezone
from datetime import timedelta


class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True, unique=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="CUSTOMER")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")

    class Meta:
        db_table = "users"


def get_expiration_time():
    return timezone.now() + timedelta(days=7)


class Token(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tokens")
    created = models.DateTimeField(auto_now_add=True)
    expires = models.DateTimeField(default=get_expiration_time)

    class Meta:
        db_table = "tokens"

    @staticmethod
    def generate_token(user):
        Token.objects.filter(user=user, expires__lt=timezone.now()).delete()

        token = secrets.token_hex(20)
        return Token.objects.create(user=user, key=token)

    def is_expired(self):
        return self.expires < timezone.now()
