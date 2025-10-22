from rest_framework import serializers
from .models import Quote, QuoteItem, Order, OrderItem
from users.models import User
from articles.models import Article
from users.serializers import UserSerializer
from articles.serializers import ArticleSerializer


class QuoteItemSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    article_id = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all(), source="article", write_only=True
    )

    class Meta:
        model = QuoteItem
        fields = [
            "id",
            "article",
            "article_id",
            "quantity",
            "price",
            "subtotal",
        ]
        read_only_fields = ["subtotal"]


class QuoteSerializer(serializers.ModelSerializer):
    quote_number = serializers.CharField(read_only=True)
    customer = UserSerializer(read_only=True)
    seller = UserSerializer(read_only=True)
    items = QuoteItemSerializer(many=True, read_only=True)

    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="customer", write_only=True
    )
    seller_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="seller", write_only=True
    )

    class Meta:
        model = Quote
        fields = [
            "id",
            "quote_number",
            "customer",
            "customer_id",
            "seller",
            "seller_id",
            "status",
            "issue_date",
            "expiration_date",
            "subtotal",
            "total",
            "notes",
            "items",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["subtotal", "total", "created_at", "updated_at"]


class QuoteCreateSerializer(serializers.ModelSerializer):
    items = QuoteItemSerializer(many=True)

    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="customer", write_only=True
    )
    seller_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="seller", write_only=True
    )

    class Meta:
        model = Quote
        fields = [
            "id",
            "quote_number",
            "customer_id",
            "seller_id",
            "status",
            "issue_date",
            "expiration_date",
            "notes",
            "items",
        ]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        quote = Quote.objects.create(**validated_data)

        for item_data in items_data:
            QuoteItem.objects.create(quote=quote, **item_data)

        quote.calculate_totals()
        return quote


class OrderItemSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    article_id = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all(), source="article", write_only=True
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "article",
            "article_id",
            "quantity",
            "price",
            "subtotal",
        ]
        read_only_fields = ["subtotal"]


class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    seller = UserSerializer(read_only=True)
    items = OrderItemSerializer(many=True, read_only=True)

    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="customer", write_only=True
    )
    seller_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="seller", write_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "order_number",
            "customer",
            "customer_id",
            "seller",
            "seller_id",
            "status",
            "payment_status",
            "issue_date",
            "expiration_date",
            "subtotal",
            "total",
            "notes",
            "items",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["subtotal", "total", "created_at", "updated_at"]


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    customer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="customer", write_only=True
    )
    seller_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="seller", write_only=True
    )

    class Meta:
        model = Order
        fields = [
            "order_number",
            "customer_id",
            "seller_id",
            "status",
            "payment_status",
            "issue_date",
            "expiration_date",
            "notes",
            "items",
        ]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        order.calculate_totals()
        return order