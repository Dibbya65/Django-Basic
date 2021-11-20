from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes),
    path("rooms/", views.get_rooms, path("room/<str:id>", views.get_room)),
]
