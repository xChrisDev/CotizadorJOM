from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .pdf_generator import PDFGenerator


class EmailService:
    """Servicio para envío de correos electrónicos"""

    @staticmethod
    def send_quote_email(quote, recipient_email=None, cc_emails=None):
        try:
            if not recipient_email:
                recipient_email = quote.customer.email
            
            if not recipient_email:
                raise ValueError("No se proporcionó un email de destinatario")
            
            # Generar PDF
            pdf_file = PDFGenerator.generate_quote_pdf(quote)
            if not pdf_file:
                raise Exception("Error al generar el PDF")
            
            # Preparar el email
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
            
            html_body = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0;
            padding: 20px;
            text-align: left;
        }}
        .container {{
            max-width: 600px;
            margin-left: 0;
            margin-right: auto;
            padding: 0;
        }}
        .header {{
            background-color: #27ae60;
            color: white;
            padding: 10px;
            text-align: left;
            border-radius: 5px 5px 0 0;
        }}
        .content {{
            background-color: #f9f9f9;
            padding: 10px;
            border: 1px solid #ddd;
        }}
        .details {{
            background-color: white;
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid #27ae60;
        }}
        .detail-row {{
            margin: 6px 0;
        }}
        .label {{
            font-weight: bold;
            color: #27ae60;
        }}
        .footer {{
            background-color: #333;
            color: white;
            padding: 10px;
            text-align: center;
            font-size: 0.9em;
            border-radius: 0 0 5px 5px;
        }}
        .signature {{
            margin-top: 20px;
            padding-top: 10px;
            border-top: 2px solid #ddd;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Cotización {quote.quote_number}</h1>
        </div>
        
        <div class="content">
            <p>Estimado/a <strong>{quote.customer.first_name} {quote.customer.last_name}</strong>,</p>
            <p>Le enviamos adjunta la cotización <strong>{quote.quote_number}</strong> con los detalles solicitados.</p>
            
            <div class="details">
                <h3 style="color: #27ae60; margin-top: 0;">Detalles de la Cotización</h3>
                
                <div class="detail-row">
                    <span class="label">Número:</span> {quote.quote_number}
                </div>
                <div class="detail-row">
                    <span class="label">Fecha de emisión:</span> {quote.issue_date.strftime('%d/%m/%Y')}
                </div>
                <div class="detail-row">
                    <span class="label">Fecha de vencimiento:</span> {quote.expiration_date.strftime('%d/%m/%Y')}
                </div>
            </div>
            
            <p>Para cualquier duda o aclaración, no dude en contactarnos.</p>
            
            <div class="signature">
                <p><strong>Atentamente,</strong></p>
                <p><strong>{quote.seller.first_name} {quote.seller.last_name}</strong><br>
                Refaccionaria JOM</p>
            </div>
        </div>
        
        <div class="footer">
            <p>Este es un correo automático, por favor no responder directamente.</p>
            <p>📧 {quote.seller.email} | 📞 {quote.seller.phone_number}</p>
        </div>
    </div>
</body>
</html>
            """
            
            email = EmailMultiAlternatives(
                subject=subject,
                body=text_body,  # Texto plano como fallback
                from_email=settings.EMAIL_HOST_USER,
                to=[recipient_email],
                cc=cc_emails if cc_emails else [],
            )
            
            email.attach_alternative(html_body, "text/html")
            
            email.attach(
                f"JOM_COTIZACION_{quote.quote_number}.pdf",
                pdf_file.read(),
                "application/pdf"
            )
            
            email.send()
            
            return True
            
        except Exception as e:
            print(f"Error al enviar email de cotización: {str(e)}")
            return False