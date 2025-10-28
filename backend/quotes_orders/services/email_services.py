from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .pdf_generator import PDFGenerator
from django.template.loader import render_to_string


class EmailService:
    @staticmethod
    def send_quote_email(quote, recipient_email=None, cc_emails=None):
        try:
            if not recipient_email:
                recipient_email = quote.customer.email

            if not recipient_email:
                raise ValueError("No se proporcionó un email de destinatario")

            pdf_file = PDFGenerator.generate_quote_pdf(quote)
            if not pdf_file:
                raise Exception("Error al generar el PDF")

            subject = f"Cotización {quote.quote_number} - Refaccionaria JOM"

            text_body = f"""
                Estimado/a {quote.customer.first_name} {quote.customer.last_name},

                Le enviamos adjunta la cotización {quote.quote_number} con los detalles solicitados.

                Detalles de la cotización:
                - Número: {quote.quote_number}
                - Fecha de emisión: {quote.issue_date.strftime('%d/%m/%Y')}
                - Fecha de vencimiento: {quote.expiration_date.strftime('%d/%m/%Y')}

                Para cualquier duda o aclaración, no dude en contactarnos.

                Atentamente,
                {quote.seller.first_name} {quote.seller.last_name}
                Refaccionaria JOM

                ---
                Este es un correo automático, por favor no responder directamente.
                Contacto: {quote.seller.email} | Tel: {quote.seller.phone_number}
            """

            context = {"quote": quote}
            html_body = render_to_string("../templates/quote_email.html", context)

            email = EmailMultiAlternatives(
                subject=subject,
                body=text_body,
                from_email=settings.EMAIL_HOST_USER,
                to=[recipient_email],
                cc=cc_emails if cc_emails else [],
            )

            email.attach_alternative(html_body, "text/html")

            email.attach(
                f"JOM_COTIZACION_{quote.quote_number}.pdf",
                pdf_file.read(),
                "application/pdf",
            )

            email.send()

            return True

        except Exception as e:
            print(f"Error al enviar email de cotización: {str(e)}")
            return False
