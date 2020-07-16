from django.urls import path
from rooms import views as room_veiws

app_name = 'core'

urlpatterns = [
    path("", room_veiws.all_rooms, name='home')
]