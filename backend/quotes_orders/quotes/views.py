from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import FileResponse
from django.db.models import Count, Sum, Subquery, OuterRef
from .models import Quote, Status
from .serializers import QuoteSerializer, QuoteCreateSerializer, QuoteListSerializer
from .filters import QuoteFilter
from quotes_orders.services.pdf_generator import PDFGenerator
from quotes_orders.services.email_services import EmailService
from users.permissions import IsAuth
from users.pagination import PageNumberPagination
from django.core.paginator import Paginator
from collections import defaultdict

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
        elif self.action == "list" or self.action == "quotes_by_customer" or self.action == "quotes_by_seller" or self.action == "customer_all":
            return QuoteListSerializer
        elif self.action in ["retrieve", "update", "partial_update"]:
            return QuoteSerializer

    @action(detail=False, methods=["get"], url_path="customer/(?P<customer_id>\d+)")
    def quotes_by_customer(self, request, customer_id=None):
        queryset = self.filter_queryset(self.get_queryset().filter(customer_id=customer_id))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="seller/(?P<seller_id>\d+)")
    def quotes_by_seller(self, request, seller_id=None):
        queryset = self.filter_queryset(self.get_queryset().filter(seller_id=seller_id))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["get"], url_path="customer/all")
    def customer_all(self, request):
        queryset = self.get_queryset()

        latest_status = self.get_queryset().model.status_history.rel.related_model.objects.filter(
            quote_id=OuterRef('id')
        ).order_by('-date')

        queryset = queryset.annotate(
            current_status_name=Subquery(latest_status.values('status__name')[:1])
        )

        summary_data_list = list(queryset.values(
            'customer__name',
            'current_status_name'
        ).annotate(
            quotes_count=Count('id'),
            quotes_total=Sum('total')
        ).order_by('current_status_name', 'customer__name'))
        
        grouped_result = defaultdict(list)
        for item in summary_data_list:
            status_name = item['current_status_name']
            if status_name: 
                grouped_result[status_name].append({
                    "customer_name": item['customer__name'],
                    "quotes_count": item['quotes_count'],
                    "quotes_total": item['quotes_total']
                })

        paginable_data = list(grouped_result.items())

        paginator = self.paginator
        
        if not paginator:
            paginator = Paginator(paginable_data, 10)

        page = self.paginate_queryset(paginable_data) 
        
        if page is not None:
            paginated_result_dict = dict(page)
            
            return self.get_paginated_response(paginated_result_dict)

        return Response(dict(grouped_result), status=status.HTTP_200_OK)


    @action(detail=True, methods=["post"], url_path="change-status")
    def change_status(self, request, pk=None):
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

    @action(detail=True, methods=["get"], url_path="pdf")
    def generate_pdf(self, request, pk=None):
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