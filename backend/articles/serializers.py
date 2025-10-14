from rest_framework import serializers
from .models import Article, Category, Family, Brand


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

    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            "id",
            "item_code",
            "article_name",
            "unit_of_measure",
            "price_A",
            "price_B",
            "price_C",
            "category",
            "category_id",
            "family",
            "family_id",
            "brand",
            "brand_id",
            "description",
            "image",
            "image_url",
        ]

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and hasattr(obj.image, "url"):
            return request.build_absolute_uri(obj.image.url)
        return None
