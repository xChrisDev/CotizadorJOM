import django_filters
from django.db.models import Q
from .models import User


class UserFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method="filter_search", label="Search")
    status = django_filters.CharFilter(field_name="status", lookup_expr="iexact")
    ordering = django_filters.OrderingFilter(
        fields=(
            ("username", "username"),
            ("first_name", "first_name"),
            ("last_name", "last_name"),
            ("status", "status"),
        )
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "status"]

    def filter_search(self, queryset, name, value):
        terms = value.split()
        query = Q()
        for term in terms:
            query |= Q(username__icontains=term)
            query |= Q(first_name__icontains=term)
            query |= Q(last_name__icontains=term)
        return queryset.filter(query)
