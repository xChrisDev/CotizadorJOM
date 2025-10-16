from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.http import FileResponse
from .models import Quote, QuoteItem, Order, OrderItem
from .serializers import (
    QuoteSerializer,
    QuoteCreateSerializer,
    QuoteItemSerializer,
    OrderSerializer,
    OrderCreateSerializer,
    OrderItemSerializer,
)
from .filters import QuoteFilter, OrderFilter
from .pdf_generator import PDFGenerator
from users.permissions import IsAuth
from users.pagination import PageNumberPagination


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAuth]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = QuoteFilter
    search_fields = ["quote_number", "customer__username", "seller__username"]
    ordering_fields = [
        "quote_number",
        "issue_date",
        "expiration_date",
        "status",
        "total",
    ]
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action == "create":
            return QuoteCreateSerializer
        return QuoteSerializer

    @action(detail=True, methods=["get"], url_path="pdf")
    def generate_pdf(self, request, pk=None):
        """Genera y devuelve el PDF de la cotización"""
        quote = self.get_object()
        pdf_file = PDFGenerator.generate_quote_pdf(quote)

        response = FileResponse(
            pdf_file, content_type="application/pdf", as_attachment=False
        )
        response["Content-Disposition"] = (
            f'inline; filename="cotizacion_{quote.quote_number}.pdf"'
        )
        return response

    @action(detail=True, methods=["get"], url_path="download")
    def download_pdf(self, request, pk=None):
        """Descarga el PDF de la cotización"""
        quote = self.get_object()
        pdf_file = PDFGenerator.generate_quote_pdf(quote)

        response = FileResponse(
            pdf_file, content_type="application/pdf", as_attachment=True
        )
        response["Content-Disposition"] = (
            f'attachment; filename="cotizacion_{quote.quote_number}.pdf"'
        )
        return response

    @action(
        detail=False, methods=["get"], url_path="by_customer/(?P<customer_id>[^/.]+)"
    )
    def get_by_customer(self, request, customer_id=None):
        """Obtiene todas las cotizaciones de un cliente"""
        quotes = self.queryset.filter(customer__id=customer_id)
        filtered_quotes = QuoteFilter(request.GET, queryset=quotes).qs

        if not filtered_quotes.exists():
            return Response(
                {"error": f"No se encontraron cotizaciones para el cliente {customer_id}."},
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.paginate_queryset(filtered_quotes)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_quotes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="by_seller/(?P<seller_id>[^/.]+)")
    def get_by_seller(self, request, seller_id=None):
        """Obtiene todas las cotizaciones de un vendedor"""
        quotes = self.queryset.filter(seller__id=seller_id)
        filtered_quotes = QuoteFilter(request.GET, queryset=quotes).qs

        if not filtered_quotes.exists():
            return Response(
                {"error": f"No se encontraron cotizaciones para el vendedor {seller_id}."},
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.paginate_queryset(filtered_quotes)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_quotes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="by_status/(?P<quote_status>[^/.]+)")
    def get_by_status(self, request, quote_status=None):
        """Obtiene todas las cotizaciones por estado"""
        quotes = self.queryset.filter(status=quote_status.upper())
        filtered_quotes = QuoteFilter(request.GET, queryset=quotes).qs

        if not filtered_quotes.exists():
            return Response(
                {"error": f"No se encontraron cotizaciones con estado {quote_status}."},
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.paginate_queryset(filtered_quotes)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_quotes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuth]
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_class = OrderFilter
    search_fields = ["order_number", "customer__username", "seller__username"]
    ordering_fields = [
        "order_number",
        "issue_date",
        "expiration_date",
        "status",
        "payment_status",
        "total",
    ]
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action == "create":
            return OrderCreateSerializer
        return OrderSerializer

    @action(detail=True, methods=["get"], url_path="pdf")
    def generate_pdf(self, request, pk=None):
        """Genera y devuelve el PDF de la orden"""
        order = self.get_object()
        pdf_file = PDFGenerator.generate_order_pdf(order)

        response = FileResponse(
            pdf_file, content_type="application/pdf", as_attachment=False
        )
        response["Content-Disposition"] = (
            f'inline; filename="orden_{order.order_number}.pdf"'
        )
        return response

    @action(detail=True, methods=["get"], url_path="download")
    def download_pdf(self, request, pk=None):
        """Descarga el PDF de la orden"""
        order = self.get_object()
        pdf_file = PDFGenerator.generate_order_pdf(order)

        response = FileResponse(
            pdf_file, content_type="application/pdf", as_attachment=True
        )
        response["Content-Disposition"] = (
            f'attachment; filename="orden_{order.order_number}.pdf"'
        )
        return response

    @action(
        detail=False, methods=["get"], url_path="by_customer/(?P<customer_id>[^/.]+)"
    )
    def get_by_customer(self, request, customer_id=None):
        """Obtiene todas las órdenes de un cliente"""
        orders = self.queryset.filter(customer__id=customer_id)
        filtered_orders = OrderFilter(request.GET, queryset=orders).qs

        if not filtered_orders.exists():
            return Response(
                {"error": f"No se encontraron órdenes para el cliente {customer_id}."},
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.paginate_queryset(filtered_orders)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="by_seller/(?P<seller_id>[^/.]+)")
    def get_by_seller(self, request, seller_id=None):
        """Obtiene todas las órdenes de un vendedor"""
        orders = self.queryset.filter(seller__id=seller_id)
        filtered_orders = OrderFilter(request.GET, queryset=orders).qs

        if not filtered_orders.exists():
            return Response(
                {"error": f"No se encontraron órdenes para el vendedor {seller_id}."},
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.paginate_queryset(filtered_orders)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="by_status/(?P<order_status>[^/.]+)")
    def get_by_status(self, request, order_status=None):
        """Obtiene todas las órdenes por estado"""
        orders = self.queryset.filter(status=order_status.upper())
        filtered_orders = OrderFilter(request.GET, queryset=orders).qs

        if not filtered_orders.exists():
            return Response(
                {"error": f"No se encontraron órdenes con estado {order_status}."},
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.paginate_queryset(filtered_orders)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["get"],
        url_path="by_payment_status/(?P<payment_status>[^/.]+)",
    )
    def get_by_payment_status(self, request, payment_status=None):
        """Obtiene todas las órdenes por estado de pago"""
        orders = self.queryset.filter(payment_status=payment_status.upper())
        filtered_orders = OrderFilter(request.GET, queryset=orders).qs

        if not filtered_orders.exists():
            return Response(
                {
                    "error": f"No se encontraron órdenes con estado de pago {payment_status}."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.paginate_queryset(filtered_orders)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)