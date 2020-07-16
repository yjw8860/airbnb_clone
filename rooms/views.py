from django.shortcuts import render
from datetime import datetime

def all_rooms(request):
    now = datetime.now()
    hungry = True
    return render(request,
                  template_name='all_rooms.html',
                  context={
                      'now':now,
                      'hungry':hungry})