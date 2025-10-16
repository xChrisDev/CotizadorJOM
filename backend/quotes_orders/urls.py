from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuoteViewSet, OrderViewSet

router = DefaultRouter()
router.register(r"quotes", QuoteViewSet, basename="quote")
router.register(r"orders", OrderViewSet, basename="order")

urlpatterns = [
    path("api/", include(router.urls)),
]