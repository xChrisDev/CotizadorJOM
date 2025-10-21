import django_filters
from django.db.models import Q
from .models import Article, Category, Family, Brand


class ArticleFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="filter_search", label="Search")
    category = django_filters.NumberFilter(field_name="category__id")
    family = django_filters.NumberFilter(field_name="family__id")
    brand = django_filters.NumberFilter(field_name="brand__id")
    ordering = django_filters.OrderingFilter(
        fields=(
            ("item_code", "item_code"),
            ("article_name", "article_name"),
            ("category__name", "category"),
            ("family__name", "family"),
            ("brand__name", "brand"),
        )
    )

    class Meta:
        model = Article
        fields = ["item_code", "article_name", "category", "family", "brand"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(item_code__icontains=value)
            | Q(article_name__icontains=value)
            | Q(category__name__icontains=value)
            | Q(family__name__icontains=value)
            | Q(brand__name__icontains=value)
        )