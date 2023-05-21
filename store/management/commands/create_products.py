from django.core.management.base import BaseCommand
from store.models import Product

class Command(BaseCommand):
    help = 'Create default products'

    def handle(self, *args, **options):
        objects_to_create = [
            Product(name='Potatoes', price=5, quantity=2),
            Product(name='Carrots', price=4, quantity=1),
            Product(name='Onions', price=2, quantity=1),
                ]
        Product.objects.bulk_create(objects_to_create)
        self.stdout.write('Created!')