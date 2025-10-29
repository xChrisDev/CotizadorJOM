import os
import django
import random
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()

from users.models import User

fake = Faker("es_MX")

STATUS_CHOICES = ["ACTIVE", "PENDING", "BANNED", "REJECTED"]
ROLE_CHOICES = ["STAFF", "SELLER", "CUSTOMER"]

NUM_USERS = 100

def generate_username(name: str) -> str:
    parts = name.split()
    if len(parts) >= 2:
        base = (parts[0][0] + parts[1]).lower()
    else:
        base = parts[0].lower()
    return base + str(random.randint(1, 99))


for _ in range(NUM_USERS):
    role = random.choice(ROLE_CHOICES)
    status = random.choice(STATUS_CHOICES)
    name = fake.first_name() + " " + fake.last_name()

    user_data = {
        "username": generate_username(name),
        "name": name,
        "status": status,
        "role": role,
        "type": "PERSON",
        "email": fake.email(),
        "phone_number": "+52" + str(random.randint(1000000000, 9999999999)),
    }

    User.objects.create(**user_data)

for _ in range(NUM_USERS):
    role = "CUSTOMER"
    status = random.choice(STATUS_CHOICES)
    name = fake.company()

    user_data = {
        "username": generate_username(name),
        "name": name,
        "status": status,
        "role": role,
        "type": "BUSINESS",
        "email": fake.company_email(),
        "phone_number": "+52" + str(random.randint(1000000000, 9999999999)),
    }

    User.objects.create(**user_data)

print("✔ Usuarios creados correctamente.")
