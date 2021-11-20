from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('room/<str:pk>', views.roomdetail, name="room-detail"),
    path('create/room/', views.create_room, name="create-room"),
    path('update/room/<str:pk>/', views.update_room, name="update-room")
]
