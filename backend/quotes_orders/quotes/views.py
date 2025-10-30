from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import FileResponse
from .models import Quote, Status
from .serializers import QuoteSerializer, QuoteCreateSerializer, QuoteListSerializer
from .filters import QuoteFilter
from quotes_orders.services.pdf_generator import PDFGenerator
from quotes_orders.services.email_services import EmailService
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
        elif self.action == "list":
            return QuoteListSerializer
        elif self.action in ["retrieve", "update", "partial_update"]:
            return QuoteSerializer

    @action(detail=True, methods=["post"], url_path="change-status")
    def change_status(self, request, pk=None):
        """Cambia el estado de una cotización"""
        quote = self.get_object()
        status_id = request.data.get("status_id")
        note = request.data.get("note", "")

        if not status_id:
            return Response(
                {"error": "Se requiere status_id"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            new_status = Status.objects.get(id=status_id)
        except Status.DoesNotExist:
            return Response(
                {"error": "Estado no válido"}, status=status.HTTP_404_NOT_FOUND
            )

        QuoteStatus.objects.create(
            quote=quote, status=new_status, note=note, created_by=request.user
        )

        serializer = self.get_serializer(quote)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"], url_path="status-history")
    def status_history(self, request, pk=None):
        """Obtiene el historial completo de estados de una cotización"""
        quote = self.get_object()
        history = quote.status_history.all()
        serializer = QuoteStatusSerializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="by_status/(?P<status_name>[^/.]+)")
    def get_by_status(self, request, status_name=None):
        """Obtiene todas las cotizaciones por estado actual"""
        try:
            status_obj = Status.objects.get(name=status_name.upper())
        except Status.DoesNotExist:
            return Response(
                {"error": f"Estado '{status_name}' no encontrado."},
                status=status.HTTP_404_NOT_FOUND,
            )

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

    @action(detail=True, methods=["post"], url_path="send-email")
    def send_email(self, request, pk=None):
        quote = self.get_object()
        recipient_email = request.data.get("recipient_email")
        cc_emails = request.data.get("cc_emails", [])

        success = EmailService.send_quote_email(
            quote=quote, recipient_email=recipient_email, cc_emails=cc_emails
        )

        if success:
            return Response(
                {"message": "Cotización enviada por email correctamente"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Error al enviar el email"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @action(
        detail=False, methods=["get"], url_path="by_customer/(?P<customer_id>[^/.]+)"
    )
    def get_by_customer(self, request, customer_id=None):
        """Obtiene todas las cotizaciones de un cliente"""
        quotes = self.queryset.filter(customer__id=customer_id)
        filtered_quotes = QuoteFilter(request.GET, queryset=quotes).qs

        if not filtered_quotes.exists():
            return Response(
                {
                    "error": f"No se encontraron cotizaciones para el cliente {customer_id}."
                },
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
                {
                    "error": f"No se encontraron cotizaciones para el vendedor {seller_id}."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        page = self.paginate_queryset(filtered_quotes)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_quotes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False, methods=["get"], url_path="by_status/(?P<quote_status>[^/.]+)"
    )
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
