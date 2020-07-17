from django.views.generic import ListView
from django.urls import reverse
from rooms.models import Room
from django.utils import timezone
from django.shortcuts import render, redirect

class HomeView(ListView):

    """ HomeView Definition """

    model = Room
    paginate_by = 10
    ordering = 'created'
    paginate_orphans = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context['now'] = now
        return context


def room_detail(request, pk):
    try:
        room = Room.objects.get(pk=pk)
        return render(request, 'rooms/detail.html',
                      context={'room': room})
    except Room.DoesNotExist:
        return redirect(reverse("core:home"))


