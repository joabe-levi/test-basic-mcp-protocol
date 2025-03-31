import random, datetime
from faker import Faker
from django.core.management.base import BaseCommand
from automobile.models import Automobile
from automobile.choices import ChoiceFuel, ChoiceTransmission

fake = Faker()


class Command(BaseCommand):
    help = "Populates the Automobile table with fake data"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, nargs='?', default=100, help="Number of automobiles to create")
        
    def _calculate_depreciation_factor(self):
        return (1 - (datetime.date.today().year - random.randint(1990, datetime.date.today().year)) * 0.05)

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        automobiles = [
            Automobile(
                model=fake.word().capitalize(),
                brand=fake.company(),
                color=fake.color_name(),
                fuel_type=random.choice([choice[0] for choice in ChoiceFuel.choices]),
                engine=f"{random.randint(1, 5)}.{random.randint(0, 9)}L {random.choice(['Turbo', 'Hybrid', 'Electric', 'V8', 'V6'])}",
                transmission=random.choice([choice[0] for choice in ChoiceTransmission.choices]),
                num_doors=random.randint(2, 5),
                num_seats=random.randint(2, 7),
                year=random.randint(1990, datetime.date.today().year),
                mileage=round(random.uniform(0, 300000), 2),
                price=round(abs(random.uniform(10000, 100000) * self._calculate_depreciation_factor(), 2))
            ) for _ in range(count)
        ]
            
        Automobile.objects.bulk_create(automobiles)
        
        self.stdout.write(self.style.SUCCESS(f"Successfully created {count} automobiles!"))
