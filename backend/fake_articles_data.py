import os
import django
import random
from faker import Faker
from decimal import Decimal
import requests
from django.core.files import File
from io import BytesIO

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()

from articles.models import Article, Category, Family, Brand

fake = Faker("es_MX")

CATEGORIAS = ["Motor", "Frenos", "Suspensión", "Eléctrico", "Carrocería"]
categories_objs = []

for cat_name in CATEGORIAS:
    cat, created = Category.objects.get_or_create(name=cat_name)
    categories_objs.append(cat)
    if created:
        print(f"  ✓ {cat_name}")

FAMILIAS = [
    "Filtros",
    "Bujías",
    "Correas",
    "Aceites",
    "Pastillas",
    "Discos",
    "Amortiguadores",
    "Baterías",
    "Luces",
    "Parabrisas",
]
families_objs = []

for fam_name in FAMILIAS:
    fam, created = Family.objects.get_or_create(name=fam_name)
    families_objs.append(fam)
    if created:
        print(f"  ✓ {fam_name}")

MARCAS = [
    "Bosch",
    "Valeo",
    "ACDelco",
    "NGK",
    "Monroe",
    "KYB",
    "Pioneer",
    "Exedy",
    "Fram",
    "Hella",
]
brands_objs = []

for marca_name in MARCAS:
    marca, created = Brand.objects.get_or_create(name=marca_name)
    brands_objs.append(marca)
    if created:
        print(f"  ✓ {marca_name}")

UNIDADES = ["PZA", "KIT", "LT", "JGO", "M"]
NUM_ARTICLES = 50

for i in range(NUM_ARTICLES):
    item_code = f"REF-{str(i+1).zfill(5)}"
    article_name = f"{fake.word().capitalize()} {random.choice(FAMILIAS)}"
    unit_of_measure = random.choice(UNIDADES)

    precio_base = Decimal(random.uniform(100, 8000)).quantize(Decimal("0.01"))
    price_A = precio_base
    price_B = (precio_base * Decimal("0.95")).quantize(Decimal("0.01"))
    price_C = (precio_base * Decimal("0.90")).quantize(Decimal("0.01"))

    category = random.choice(categories_objs)
    family = random.choice(families_objs)
    brand = random.choice(brands_objs)

    description = fake.text(max_nb_chars=150)

    image_url = f"https://picsum.photos/seed/{i}/400/300"
    response = requests.get(image_url)
    image_file = File(BytesIO(response.content), name=f"{item_code}.jpg")

    Article.objects.create(
        item_code=item_code,
        article_name=article_name,
        unit_of_measure=unit_of_measure,
        price_A=price_A,
        price_B=price_B,
        price_C=price_C,
        category=category,
        family=family,
        brand=brand,
        description=description,
        image=image_file,
    )

    if (i + 1) % 25 == 0:
        print(f"  ✓ {i + 1}/{NUM_ARTICLES} artículos creados...")

print(f"\n{NUM_ARTICLES} artículos creados correctamente.")
print(f"Resumen:")
print(f"   - Categorías: {Category.objects.count()}")
print(f"   - Familias: {Family.objects.count()}")
print(f"   - Marcas: {Brand.objects.count()}")
print(f"   - Artículos: {Article.objects.count()}")
