from io import BytesIO
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from decimal import Decimal, ROUND_HALF_UP
from .enums import BANK_INFO, COMPANY_INFO, TERMS_AND_CONDITIONS
from num2words import num2words


class PDFGenerator:
    @staticmethod
    def value_to_text(valor_str):
        if isinstance(valor_str, (Decimal, int, float)):
             valor_str = str(valor_str)
        elif isinstance(valor_str, str):
             valor_str = valor_str.replace(',', '')
             
        try:
            value = Decimal(valor_str)
        except:
            return "Valor no válido"

        value = round(value, 2)
        integer_part = value.quantize(Decimal("1."), rounding="ROUND_DOWN")
        cents = int((value - integer_part) * 100)
        full_text = num2words(int(integer_part), lang="es")
        text_format = f"{full_text.capitalize()} pesos {cents:02d}/100 MXN"

        return text_format

    @staticmethod
    def fmt_decimal(value: Decimal) -> str:
        if value is None:
            return "0.00"

        if not isinstance(value, Decimal):
            value = Decimal(str(value))
        value = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        return f"{value:,.2f}"

    @staticmethod
    def generate_quote_pdf(quote):
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
            "total_text": PDFGenerator.value_to_text(quote.total),
            "company_info": COMPANY_INFO,
            "bank_info": BANK_INFO,
            "terms": TERMS_AND_CONDITIONS,
            "title": "COTIZACIÓN",
        }

        html_string = render_to_string("../templates/quote_pdf.html", context)

        pdf_file = BytesIO()
        pisa_status = pisa.CreatePDF(html_string, dest=pdf_file)

        if pisa_status.err:
            return None

        pdf_file.seek(0)
        return pdf_file
