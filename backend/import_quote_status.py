import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()

from quotes_orders.quotes.models import Status


def populate_statuses():
    print("\n=== Creando estados iniciales ===")

    statuses = [
        {"name": "DRAFT", "description": "Cotización en proceso de creación o edición"},
        {"name": "ACCEPTED", "description": "Cotización aprobada por el cliente"},
        {"name": "EXPIRED", "description": "Cotización vencida por fecha límite"},
        {"name": "SENT", "description": "Cotización enviada al cliente"},
        {"name": "DELIVERED", "description": "Orden entregada al cliente"},
    ]

    created_count = 0

    for status_data in statuses:
        obj, created = Status.objects.get_or_create(
            name=status_data["name"],
            defaults={"description": status_data["description"]},
        )

        if created:
            created_count += 1
            print(f"✓ Estado creado: {obj.name}")
        else:
            print(f"- Estado ya existe: {obj.name}")

    print(f"\nTotal estados creados: {created_count}")
    print(f"Total estados disponibles: {Status.objects.count()}")
    print("\n✅ ¡Proceso completado!")


if __name__ == "__main__":
    populate_statuses()
