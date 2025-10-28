from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .quotes.views import QuoteViewSet

router = DefaultRouter()
router.register(r"quotes", QuoteViewSet, basename="quote")

urlpatterns = [
    path("api/", include(router.urls)),
]