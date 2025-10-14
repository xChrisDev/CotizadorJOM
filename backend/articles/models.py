from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "categories"


class Family(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "families"


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "brands"


class Article(models.Model):
    item_code = models.CharField(max_length=50, unique=True)
    article_name = models.CharField(max_length=200)
    unit_of_measure = models.CharField(max_length=20)
    price_A = models.DecimalField(max_digits=10, decimal_places=2)
    price_B = models.DecimalField(max_digits=10, decimal_places=2)
    price_C = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    family = models.ForeignKey(Family, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="articles/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "articles"
