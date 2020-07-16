from django.shortcuts import render
from rooms.models import Room
from math import ceil


def all_rooms(request):
    page = int(request.GET.get('page', 1))
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = Room.objects.all()[offset:limit]
    page_count = ceil(Room.objects.count() / page_size)
    page_count_range = range(1, page_count+1)
    return render(request,
                  template_name='rooms/home.html',
                  context={
                  'all_rooms':all_rooms,
                  'page':page,
                  'page_count':page_count,
                  'page_count_range':page_count_range})