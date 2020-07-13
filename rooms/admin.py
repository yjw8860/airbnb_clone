from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition"""

    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition"""

    fieldsets = (
        (
            'Spaces',
            {'fields': ('guests', 'bedrooms', 'beds', 'baths')}
        ),
        (
            'Basic Info',
            {'fields':('name', 'description', 'country', 'address', 'price')}
        ),
        (
            'Times',
            {'fields':('check_in', 'check_out', 'instant_book')}
        ),
        (
            'More About the Space',
            {'fields':('amenities','facilities','house_rules',)}
        ),
        (
            'Last Details',
            {'fields':('host',)}
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities"
    )

    list_filter = ('instant_book','host__superhost', "room_type", "amenities", "facilities", "house_rules", 'country', 'city')

    #https://docs.djangoproject.com/en/2.2/ref/contrib/admin/ 참고
    search_fields = ['=city', '^host__username']

    filter_horizontal = ('amenities','facilities','house_rules',)

    def count_amenities(self, obj):
        print(obj.amenities.all())
        return "potato"
    count_amenities.short_description = 'HELLO SEXY?'

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition"""

    pass
