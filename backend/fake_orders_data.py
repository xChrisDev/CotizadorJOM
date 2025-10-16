import os
import django
import random
from faker import Faker
from decimal import Decimal
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()

from quotes_orders.models import Order, OrderItem
from users.models import User
from articles.models import Article
from django.utils import timezone

fake = Faker("es_MX")

# Obtener usuarios existentes
customers = list(User.objects.filter(role="CUSTOMER", status="ACTIVE"))
sellers = list(User.objects.filter(role__in=["SELLER", "STAFF", "ADMIN"]))
articles = list(Article.objects.all())

if not customers:
    print("⚠️ No hay clientes activos. Crea usuarios primero.")
    exit()

if not sellers:
    print("⚠️ No hay vendedores. Crea usuarios con rol SELLER, STAFF o ADMIN.")
    exit()

if not articles:
    print("⚠️ No hay artículos. Crea artículos primero.")
    exit()

STATUS_CHOICES = ["PENDING", "APPROVED", "REJECTED", "EXPIRED"]
PAYMENT_STATUS_CHOICES = ["PENDING", "PARTIAL", "PAID", "CANCELLED"]
NUM_ORDERS = 25

print("Creando órdenes de compra...")

for i in range(NUM_ORDERS):
    order_number = f"ORD-{str(i + 1).zfill(5)}"
    customer = random.choice(customers)
    seller = random.choice(sellers)
    status = random.choice(STATUS_CHOICES)
    payment_status = random.choice(PAYMENT_STATUS_CHOICES)
    
    issue_date = timezone.now().date() - timedelta(days=random.randint(0, 45))
    expiration_date = issue_date + timedelta(days=15)
    
    notes = fake.text(max_nb_chars=200) if random.random() > 0.5 else None
    
    order = Order.objects.create(
        order_number=order_number,
        customer=customer,
        seller=seller,
        status=status,
        payment_status=payment_status,
        issue_date=issue_date,
        expiration_date=expiration_date,
        notes=notes,
    )
    
    # Crear items para la orden
    num_items = random.randint(2, 8)
    selected_articles = random.sample(articles, min(num_items, len(articles)))
    
    for article in selected_articles:
        quantity = Decimal(random.randint(1, 20))
        # Usar uno de los tres precios del artículo
        price_choice = random.choice([article.price_A, article.price_B, article.price_C])
        
        OrderItem.objects.create(
            order=order,
            article=article,
            quantity=quantity,
            price=price_choice,
        )
    
    if (i + 1) % 10 == 0:
        print(f"  ✓ {i + 1}/{NUM_ORDERS} órdenes creadas...")

print(f"\n✅ {NUM_ORDERS} órdenes de compra creadas correctamente.")
print(f"Resumen:")
print(f"   - Órdenes totales: {Order.objects.count()}")
print(f"   - Items de orden: {OrderItem.objects.count()}")