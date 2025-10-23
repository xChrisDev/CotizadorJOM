import django_filters
from django.db.models import Q
from .models import Quote, Order


class QuoteFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="filter_search", label="Search")
    status = django_filters.CharFilter(field_name="status", lookup_expr="iexact")
    customer = django_filters.NumberFilter(field_name="customer__id")
    seller = django_filters.NumberFilter(field_name="seller__id")
    issue_date = django_filters.DateFromToRangeFilter()
    expiration_date = django_filters.DateFromToRangeFilter()

    ordering = django_filters.OrderingFilter(
        fields=[
            ("quote_number", "quote_number"),
            ("issue_date", "issue_date"),
            ("expiration_date", "expiration_date"),
            ("status", "status"),
            ("total", "total"),
        ]
    )

    class Meta:
        model = Quote
        fields = [
            "quote_number",
            "status",
            "customer",
            "seller",
            "issue_date",
            "expiration_date",
        ]

    def filter_search(self, queryset, name, value):
        """Permite buscar por nombre completo o parcial."""
        terms = value.strip().split()
        q = (
            Q(quote_number__icontains=value)
            | Q(customer__username__icontains=value)
            | Q(seller__username__icontains=value)
        )

        if len(terms) == 1:
            q |= Q(customer__first_name__icontains=terms[0]) | Q(
                customer__last_name__icontains=terms[0]
            )
        elif len(terms) >= 2:
            q |= Q(
                customer__first_name__icontains=terms[0],
                customer__last_name__icontains=terms[-1],
            )

        return queryset.filter(q)

    def filter_queryset(self, queryset):
        """Optimiza las consultas para evitar N+1 queries."""
        queryset = queryset.select_related("customer", "seller")
        return super().filter_queryset(queryset)


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
