from django.db import models, transaction
from users.models import User
from articles.models import Article
from .enums import STATUS_CHOICES, PAYMENT_STATUS_CHOICES
from django.utils import timezone
from decimal import Decimal


class QuoteCounter(models.Model):
    """Contador global para quotes"""

    last_number = models.PositiveIntegerField(default=0)


class Quote(models.Model):
    quote_number = models.CharField(max_length=50, unique=True, blank=True)
    customer = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="quotes_as_customer"
    )
    seller = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="quotes_as_seller"
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")
    issue_date = models.DateField(default=timezone.now)
    expiration_date = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.quote_number:
            with transaction.atomic():
                counter, created = (
                    QuoteCounter.objects.select_for_update().get_or_create(id=1)
                )
                counter.last_number += 1
                self.quote_number = f"COT-{counter.last_number:04d}"
                counter.save()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "quotes"
        ordering = ["-created_at"]

    def calculate_totals(self):
        items = self.items.all()
        self.total = sum(Decimal(item.subtotal) for item in items)
        self.subtotal = self.total / Decimal("1.16")
        self.save()

    def __str__(self):
        return f"Quote {self.quote_number}"


class QuoteItem(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name="items")
    article = models.ForeignKey(Article, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "quote_items"

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.price
        super().save(*args, **kwargs)
        self.quote.calculate_totals()

    def __str__(self):
        return f"{self.article.article_name} - {self.quantity}"


class Order(models.Model):
    order_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="orders_as_customer"
    )
    seller = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="orders_as_seller"
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")
    payment_status = models.CharField(
        max_length=10, choices=PAYMENT_STATUS_CHOICES, default="PENDING"
    )
    issue_date = models.DateField(default=timezone.now)
    expiration_date = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "orders"
        ordering = ["-created_at"]

    def calculate_totals(self):
        items = self.items.all()
        self.subtotal = sum(item.subtotal for item in items)
        self.total = self.subtotal
        self.save()

    def __str__(self):
        return f"Order {self.order_number}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    article = models.ForeignKey(Article, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "order_items"

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.price
        super().save(*args, **kwargs)
        self.order.calculate_totals()

    def __str__(self):
        return f"{self.article.article_name} - {self.quantity}"
