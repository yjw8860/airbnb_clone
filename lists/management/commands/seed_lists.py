from django_seed import Seed
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from lists.models import List
from users.models import User
from rooms.models import Room
import random

NAME = 'lists'

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
        seeder.add_entity(List, number, {
            'user':lambda x: random.choice(user)
        })
        created_lists = seeder.execute()
        cleaned_lists = flatten(list(created_lists.values()))
        for pk in cleaned_lists:
            list_model = List.objects.get(pk=pk)
            to_add = room[random.randint(0,5): random.randint(6,30)]
            list_model.room.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f'{number} {NAME} are created!'))
