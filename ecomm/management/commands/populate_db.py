from django.core.management.base import BaseCommand
from faker import Faker

from ecomm.models import Product, Purchase
from util.progress_bar_util import print_progress_bar


class Command(BaseCommand):
    help = "Populates the database with sample data."

    def add_arguments(self, parser):
        parser.add_argument("--amount", type=int, help="The number of purchases that should be created.")

    def handle(self, *args, **options):
        fake = Faker()
        amount = options["amount"] if options["amount"] else 1_000_000

        # Create a few products
        if Product.objects.count() == 0:
            Product.objects.bulk_create([
                Product(name="T-shirt", description="Comfortable cotton T-shirt for everyday wear.", price=20),
                Product(name="Hoodie", description="Warm and cozy hoodie for chilly days.", price=40),
                Product(name="Socks", description="Breathable cotton socks for all seasons.", price=10),
                Product(name="Sneakers", description="Stylish sneakers for casual wear.", price=60),
                Product(name="Jeans", description="Classic blue jeans for a timeless look.", price=50),
                Product(name="Tie", description="Elegant silk tie for formal occasions.", price=30),
                Product(name="Watch", description="Sleek analog watch for everyday use.", price=100),
                Product(name="Backpack", description="Durable backpack for work or travel.", price=80),
            ])
            print("Successfully created a few products.")

        products = Product.objects.all()
        products_count = products.count()

        # Create `amount` of purchases
        print("Moving onto creation of purchases. This may take a while...")
        bulk_count = 2_500
        count = 0
        while count < amount:
            print_progress_bar(count, amount + 1)
            purchases = [
                Purchase(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    address=fake.address(),
                    product=products[fake.random_int(min=0, max=products_count - 1)]
                )
                for _ in range(bulk_count)
            ]
            Purchase.objects.bulk_create(purchases)
            count += bulk_count

        print("")
        print("Successfully populated the database.")
