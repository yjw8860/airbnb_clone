from django.shortcuts import render
from django.core.paginator import Paginator
from rooms.models import Room

def all_rooms(request):
    page = request.GET.get('page')
    room_list = Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    return render(request,
                  template_name='rooms/home.html',
                  context={
                  'rooms':rooms})