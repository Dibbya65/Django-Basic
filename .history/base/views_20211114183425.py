from django.shortcuts import render
from .models import Room
from .forms import RoomForm
# Create your views here.


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/room.html', context)


def roomdetail(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/single-room.html', context)


def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
