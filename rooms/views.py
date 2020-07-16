from django.shortcuts import render
from rooms.models import Room
def all_rooms(request):
    all_rooms = Room.objects.all()

    return render(request,
                  template_name='rooms/home.html',
                  context={
                      'all_rooms':all_rooms})