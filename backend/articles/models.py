from django.db import models
from .enums import PRICE_TYPE_CHOICES

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name


class Family(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "families"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "brands"

    def __str__(self):
        return self.name


class Article(models.Model):
    item_code = models.CharField(max_length=50, unique=True)
    article_name = models.CharField(max_length=200)
    unit_of_measure = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    family = models.ForeignKey(Family, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="articles/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "articles"

    def __str__(self):
        return f"{self.item_code} - {self.article_name}"


class PriceType(models.Model):
    name = models.CharField(
        max_length=20,
        choices=PRICE_TYPE_CHOICES,
        unique=True
    )
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = "price_types"
        ordering = ['id']
    
    def __str__(self):
        return self.get_name_display()


class ArticlePrice(models.Model):
    article = models.ForeignKey(
        Article, 
        on_delete=models.CASCADE, 
        related_name='prices'
    )
    price_type = models.ForeignKey(
        PriceType, 
        on_delete=models.PROTECT,
        related_name='article_prices'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        db_table = "article_prices"
        unique_together = ['article', 'price_type']
        ordering = ['price_type__id']
    
    def __str__(self):
        return f"{self.article.item_code} - {self.price_type.name}: ${self.price}"