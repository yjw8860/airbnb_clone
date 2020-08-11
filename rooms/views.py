from django.views.generic import ListView
from django.http import Http404
from rooms.models import Room, RoomType, Amenity, Facility
from django.utils import timezone
from django.shortcuts import render
from django_countries import countries


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
        raise Http404()

def search(request):
    city = request.GET.get('city', 'Anywhere')
    city = str.capitalize(city)
    country = request.GET.get('country', 'KR')
    room_type = int(request.GET.get('room_type', 0))

    price = int(request.GET.get('price', 0))
    guests = int(request.GET.get('guests', 0))
    bedrooms = int(request.GET.get('bedrooms', 0))
    beds = int(request.GET.get('beds', 0))
    baths = int(request.GET.get('baths', 0))
    s_amenity = request.GET.getlist('amenities')
    s_facility = request.GET.getlist('facilities')
    instant = bool(request.GET.get("instant", False))
    super_host = bool(request.GET.get("super_host", False))

    form = {
        's_room_type': room_type,
        's_country': country,
        "city": city,
        'price':price,
        'guests':guests,
        'bedrooms':bedrooms,
        'beds':beds,
        'baths':baths,
        's_amenity':s_amenity,
        's_facility':s_facility,
        "instant":instant,
        "super_host":super_host,
    }

    room_types = RoomType.objects.all()
    amenities = Amenity.objects.all()
    facilities = Facility.objects.all()

    choices = {
        "countries": countries,
        'room_types': room_types,
        'amenities':amenities,
        'facilities':facilities,
    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args['country'] = country

    if room_type != 0:
        filter_args["room_type__pk"] = room_type

    if price != 0:
        filter_args['price__lte'] = price

    if guests != 0:
        filter_args['guests__gt'] = guests

    if bedrooms != 0:
        filter_args['bedrooms__gt'] = bedrooms

    if beds != 0:
        filter_args['beds__gt'] = beds

    if baths != 0:
        filter_args['baths__gt'] = baths

    if instant is True:
        filter_args["instant_book"] = True


    rooms = Room.objects.filter(**filter_args)


    return render(request, "rooms/search.html", {**form, **choices, "rooms":rooms})