from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet, basename="user")
router.register(r"sellers", views.SellerViewSet, basename="seller")
router.register(r"purchasing-staff", views.PurchasingStaffViewSet, basename="purchasingstaff")
router.register(r"admins", views.AdminViewSet, basename="admin")
router.register(r"clients", views.ClientViewSet, basename="client")

urlpatterns = [
    path("login", views.login, name="login"),
    path("me", views.me, name="profile"),
    path("", include(router.urls)),
]