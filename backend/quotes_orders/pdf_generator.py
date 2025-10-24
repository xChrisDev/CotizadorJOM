from io import BytesIO
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from decimal import Decimal, ROUND_HALF_UP


class PDFGenerator:
    COMPANY_INFO = {
        "logo_url": "https://res.cloudinary.com/dxhjcaqpk/image/upload/v1760545192/JOM_q0pkvn.png",
        "razon_social": "Refaccionaria JOM",
        "direccion": "Calle Fray Servando T. de M. Ote. 211, Barrio Alto, 99070 Fresnillo, Zac.",
        "telefono": "+52 449 264 0046",
        "email": "contacto@jom.com.mx",
    }

    BANK_INFO = {
        "rfc": "JRA123456789",
        "banco": "BANORTE IXE",
        "cuenta": "0269668573",
        "clabe": "072933002696685738",
        "titular": "JOSUE MEDINA LEDESMA",
    }

    TERMS_AND_CONDITIONS = [
        "Los precios están sujetos a cambios sin previo aviso.",
        "El tiempo de entrega es de 3 a 5 días hábiles después de confirmar el pago.",
        "Las cotizaciones tienen una vigencia de 15 días naturales.",
        "No se aceptan devoluciones ni cambios en refacciones eléctricas.",
        "La garantía aplica únicamente en defectos de fabricación.",
        "Los pagos deben realizarse mediante transferencia bancaria o efectivo.",
        "El cliente debe verificar el estado de la mercancía al momento de recibirla.",
    ]

    @staticmethod
    def fmt_decimal(value: Decimal) -> str:
        """Formatea Decimal a string con 2 decimales. No muta el valor original."""
        if value is None:
            return "0.00"

        if not isinstance(value, Decimal):
            value = Decimal(str(value))
        value = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        return f"{value:,.2f}"

    @staticmethod
    def generate_quote_pdf(quote):
        """Genera PDF de una cotización usando xhtml2pdf"""

        items = [
            {
                "id": it.id,
                "article": {
                    "item_code": it.article.item_code if it.article else "",
                    "article_name": it.article.article_name if it.article else "",
                    "unit_of_measure": it.article.unit_of_measure if it.article else "",
                },
                "quantity": it.quantity,
                "price": PDFGenerator.fmt_decimal(it.price),
                "subtotal": PDFGenerator.fmt_decimal(it.subtotal),
            }
            for it in quote.items.all()
        ]

        subtotal = PDFGenerator.fmt_decimal(quote.subtotal)
        total = PDFGenerator.fmt_decimal(quote.total)
        iva = PDFGenerator.fmt_decimal(quote.total - quote.subtotal)

        context = {
            "quote": quote,
            "items": items,
            "iva": iva,
            "subtotal_fmt": subtotal,
            "total_fmt": total,
            "company_info": PDFGenerator.COMPANY_INFO,
            "bank_info": PDFGenerator.BANK_INFO,
            "terms": PDFGenerator.TERMS_AND_CONDITIONS,
            "title": "COTIZACIÓN",
        }

        html_string = render_to_string("quotes/quote_pdf.html", context)

        pdf_file = BytesIO()
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)

        if pisa_status.err:
            return None

        pdf_file.seek(0)
        return pdf_file

    @staticmethod
    def generate_order_pdf(order):
        """Genera PDF de una orden de compra usando xhtml2pdf"""
        context = {
            "order": order,
            "company_info": PDFGenerator.COMPANY_INFO,
            "bank_info": PDFGenerator.BANK_INFO,
            "terms": PDFGenerator.TERMS_AND_CONDITIONS,
            "title": "ORDEN DE COMPRA",
        }

        html_string = render_to_string("orders/order_pdf.html", context)

        pdf_file = BytesIO()
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)

        if pisa_status.err:
            return None

        pdf_file.seek(0)
        return pdf_file
