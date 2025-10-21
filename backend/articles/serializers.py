from rest_framework import serializers
from .models import Article, Category, Family, Brand, PriceType, ArticlePrice


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ["id", "name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name"]


class PriceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceType
        fields = ["id", "name", "description"]


class ArticlePriceSerializer(serializers.ModelSerializer):
    price_type_name = serializers.CharField(source='price_type.get_name_display', read_only=True)
    
    class Meta:
        model = ArticlePrice
        fields = ["id", "price_type", "price_type_name", "price"]


class ArticlePriceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlePrice
        fields = ["price_type", "price"]


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    family = FamilySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )
    family_id = serializers.PrimaryKeyRelatedField(
        queryset=Family.objects.all(), source="family", write_only=True
    )
    brand_id = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(), source="brand", write_only=True
    )

    prices = ArticlePriceSerializer(many=True, read_only=True)
    prices_data = ArticlePriceWriteSerializer(many=True, write_only=True, required=False)
    
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            "id",
            "item_code",
            "article_name",
            "unit_of_measure",
            "category",
            "category_id",
            "family",
            "family_id",
            "brand",
            "brand_id",
            "description",
            "image",
            "image_url",
            "prices",
            "prices_data",
        ]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and hasattr(obj.image, "url"):
            return request.build_absolute_uri(obj.image.url)
        return None
    
    def create(self, validated_data):
        prices_data = validated_data.pop('prices_data', [])
        article = Article.objects.create(**validated_data)
        
        for price_data in prices_data:
            ArticlePrice.objects.create(article=article, **price_data)
        
        return article
    
    def update(self, instance, validated_data):
        prices_data = validated_data.pop('prices_data', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if prices_data is not None:
            instance.prices.all().delete()
            for price_data in prices_data:
                ArticlePrice.objects.create(article=instance, **price_data)
        
        return instance