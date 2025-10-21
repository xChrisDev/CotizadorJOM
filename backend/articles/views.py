from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Article, Category, Family, Brand, PriceType
from .serializers import (
    ArticleSerializer,
    CategorySerializer,
    FamilySerializer,
    BrandSerializer,
    PriceTypeSerializer,
)
from .filters import ArticleFilter
from users.permissions import IsAuth
from users.pagination import PageNumberPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuth]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]
    pagination_class = PageNumberPagination


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [IsAuth]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]
    pagination_class = PageNumberPagination


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuth]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]
    pagination_class = PageNumberPagination


class PriceTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet de solo lectura para tipos de precio"""
    queryset = PriceType.objects.all()
    serializer_class = PriceTypeSerializer
    permission_classes = [IsAuth]
    pagination_class = None


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.prefetch_related('prices', 'prices__price_type').all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuth]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = ArticleFilter
    search_fields = ["item_code", "article_name"]
    ordering_fields = [
        "item_code",
        "article_name",
        "category__name",
        "family__name",
        "brand__name",
    ]
    pagination_class = PageNumberPagination

    @action(
        detail=False, methods=["get"], url_path="by_category/(?P<category_id>[^/.]+)"
    )
    def get_by_category(self, request, category_id=None):
        articles = self.queryset.filter(category__id=category_id)
        filtered_articles = ArticleFilter(request.GET, queryset=articles).qs

        if not filtered_articles.exists():
            return Response(
                {
                    "error": f"No se encontraron artículos en la categoría {category_id}."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.paginate_queryset(filtered_articles)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="by_family/(?P<family_id>[^/.]+)")
    def get_by_family(self, request, family_id=None):
        articles = self.queryset.filter(family__id=family_id)
        filtered_articles = ArticleFilter(request.GET, queryset=articles).qs

        if not filtered_articles.exists():
            return Response(
                {"error": f"No se encontraron artículos en la familia {family_id}."},
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.paginate_queryset(filtered_articles)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="by_brand/(?P<brand_id>[^/.]+)")
    def get_by_brand(self, request, brand_id=None):
        articles = self.queryset.filter(brand__id=brand_id)
        filtered_articles = ArticleFilter(request.GET, queryset=articles).qs

        if not filtered_articles.exists():
            return Response(
                {"error": f"No se encontraron artículos de la marca {brand_id}."},
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.paginate_queryset(filtered_articles)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)