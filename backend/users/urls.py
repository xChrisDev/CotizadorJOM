from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminViewSet, SellerViewSet, StaffViewSet, CustomerViewSet
from . import views

router = DefaultRouter()
router.register(r'admins', AdminViewSet)
router.register(r'sellers', SellerViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path("login/", views.login, name="login"),
    path("me/", views.me, name="profile"),
    path("", include(router.urls)),
]