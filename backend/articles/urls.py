from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CategoryViewSet, FamilyViewSet, BrandViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"families", FamilyViewSet, basename="family")
router.register(r"brands", BrandViewSet, basename="brand")
router.register(r"articles", ArticleViewSet, basename="article")

urlpatterns = [
    path("api/", include(router.urls)),
]