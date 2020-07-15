from django_seed import Seed
from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from reservations.models import Reservation
from users.models import User
from rooms.models import Room
import random

NAME = 'reservations'

class Command(BaseCommand):
    help = f'This command creates many {NAME}'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number', default = 1, type=int, help=f'how many {NAME} do you want to create'
        )

    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        user = User.objects.all()
        room = Room.objects.all()
        seeder.add_entity(Reservation, number, {
            'status': lambda x: random.choice(['pending','confirm','canceled']),
            'guest':lambda x: random.choice(user),
            'room': lambda x: random.choice(room),
            'check_in': lambda x: datetime.now(),
            'check_out': lambda x: datetime.now() + timedelta(days=random.randint(3, 25))
        })
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f'{number} {NAME} are created!'))
