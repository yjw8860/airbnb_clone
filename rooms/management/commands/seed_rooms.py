from django_seed import Seed
from django.core.management.base import BaseCommand
from rooms.models import Room, RoomType
from users.models import User
import random

class Command(BaseCommand):
    help = 'This command creates many users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default = 1, type=int, help='how many users do you want to create'
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        all_users = User.objects.all()
        room_types = RoomType.objects.all()
        seeder.add_entity(Room, number, {
            'name': lambda x: seeder.faker.address(),
            'host': lambda x: random.choice(all_users),
            'room_type': lambda x:random.choice(room_types),
            'price': lambda x:random.randint(100, 10000)//100 * 100,
            'beds':lambda x:random.randint(1, 5),
            'bedrooms':lambda x:random.randint(1, 5),
            'baths':lambda x:random.randint(1, 5),
            'guests':lambda x:random.randint(1, 10)
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'{number} rooms are created!'))
