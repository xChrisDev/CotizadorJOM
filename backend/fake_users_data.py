import os
import django
import random
from faker import Faker

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "server.settings"
) 
django.setup()

from users.models import User

fake = Faker("es_MX")

STATUS_CHOICES = ["ACTIVE", "PENDING", "BANNED", "REJECTED"]
ROLE_CHOICES = ["ADMIN", "STAFF", "SELLER", "CUSTOMER"]

NUM_USERS = 200

for _ in range(NUM_USERS):
    role = random.choice(ROLE_CHOICES)
    status = random.choice(STATUS_CHOICES)
    first_name = fake.first_name()
    last_name = fake.last_name() + " " + fake.last_name()
    username = (first_name[0] + last_name.split()[0]).lower() + str(
        random.randint(1, 99)
    )

    user_data = {
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "status": status,
        "role": role,
        "email": fake.email(),
        "phone_number": "+52" + str(random.randint(1000000000, 9999999999))
    }
    
    User.objects.create(**user_data)

print(f"{NUM_USERS} usuarios creados correctamente.")
