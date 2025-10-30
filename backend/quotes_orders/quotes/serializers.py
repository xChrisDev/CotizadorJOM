from rest_framework import serializers
from .models import Quote, QuoteItem, Status, QuoteStatus
from users.models import User
from users.serializers import UserSerializer, LightUserSerializer
from articles.models import Article
from articles.serializers import ArticleSerializer


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id", "name", "description"]


class LightStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ["id", "name", "description"]


class LightCurrentStatusSerializer(serializers.ModelSerializer):
    status = LightStatusSerializer()

    class Meta:
        model = QuoteStatus
        fields = ["id", "status", "date"]


class QuoteStatusSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(), source="status", write_only=True
    )
    created_by = UserSerializer(read_only=True)
    created_by_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source="created_by",
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model = QuoteStatus
        fields = [
            "id",
            "quote",
            "status",
            "status_id",
            "note",
            "date",
            "created_by",
            "created_by_id",
        ]
        read_only_fields = ["date"]


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
    current_status = serializers.SerializerMethodField()
    status_history = QuoteStatusSerializer(many=True, read_only=True)

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
            "current_status",
            "status_history",
            "issue_date",
            "expiration_date",
            "subtotal",
            "total",
            "notes",
            "items",
        ]
        read_only_fields = ["subtotal", "total"]

    def get_current_status(self, obj):
        current = obj.get_current_status()
        if current:
            return QuoteStatusSerializer(current).data
        return None


class QuoteCreateSerializer(serializers.ModelSerializer):
    items = QuoteItemSerializer(many=True)
    initial_status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(), write_only=True, required=False
    )

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
            "issue_date",
            "expiration_date",
            "notes",
            "items",
            "initial_status_id",
        ]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        initial_status = validated_data.pop("initial_status_id", None)

        quote = Quote.objects.create(**validated_data)

        # Crear items
        for item_data in items_data:
            QuoteItem.objects.create(quote=quote, **item_data)

        # Crear estado inicial
        if not initial_status:
            initial_status = Status.objects.get(name="PENDING")

        QuoteStatus.objects.create(
            quote=quote,
            status=initial_status,
            note="Estado inicial de la cotización",
            created_by=quote.seller,
        )

        quote.calculate_totals()
        return quote


class QuoteListSerializer(serializers.ModelSerializer):
    customer = LightUserSerializer()
    seller = LightUserSerializer()

    current_status = serializers.SerializerMethodField()

    class Meta:
        model = Quote
        fields = [
            "id",
            "quote_number",
            "customer",
            "seller",
            "current_status",
            "issue_date",
            "expiration_date",
            "total",
        ]

    def get_current_status(self, obj: Quote):
        status_obj = obj.get_current_status()

        if status_obj:
            return LightCurrentStatusSerializer(status_obj).data
        return None
