import django_filters
from django.db.models import Q
from .models import Quote, Order


class QuoteFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="filter_search", label="Search")
    status = django_filters.CharFilter(field_name="status", lookup_expr="iexact")
    customer = django_filters.NumberFilter(field_name="customer__id")
    seller = django_filters.NumberFilter(field_name="seller__id")
    ordering = django_filters.OrderingFilter(
        fields=(
            ("quote_number", "quote_number"),
            ("issue_date", "issue_date"),
            ("expiration_date", "expiration_date"),
            ("status", "status"),
            ("total", "total"),
        )
    )

    class Meta:
        model = Quote
        fields = ["quote_number", "status", "customer", "seller"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(quote_number__icontains=value)
            | Q(customer__username__icontains=value)
            | Q(customer__first_name__icontains=value)
            | Q(customer__last_name__icontains=value)
            | Q(seller__username__icontains=value)
        )


class OrderFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="filter_search", label="Search")
    status = django_filters.CharFilter(field_name="status", lookup_expr="iexact")
    payment_status = django_filters.CharFilter(
        field_name="payment_status", lookup_expr="iexact"
    )
    customer = django_filters.NumberFilter(field_name="customer__id")
    seller = django_filters.NumberFilter(field_name="seller__id")
    ordering = django_filters.OrderingFilter(
        fields=(
            ("order_number", "order_number"),
            ("issue_date", "issue_date"),
            ("expiration_date", "expiration_date"),
            ("status", "status"),
            ("payment_status", "payment_status"),
            ("total", "total"),
        )
    )

    class Meta:
        model = Order
        fields = ["order_number", "status", "payment_status", "customer", "seller"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(order_number__icontains=value)
            | Q(customer__username__icontains=value)
            | Q(customer__first_name__icontains=value)
            | Q(customer__last_name__icontains=value)
            | Q(seller__username__icontains=value)
        )