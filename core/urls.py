from django.urls import path
from rooms import views as room_veiws

app_name = 'core'

urlpatterns = [
    path("", room_veiws.HomeView.as_view(), name='home')
]