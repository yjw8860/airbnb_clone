from django.shortcuts import render
from rooms.models import Room


def all_rooms(request):
    page = int(request.GET.get('page', 1))
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = Room.objects.all()[offset:limit]

    return render(request,
                  template_name='rooms/home.html',
                  context={
                      'all_rooms':all_rooms})