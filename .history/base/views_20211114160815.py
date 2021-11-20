from django.shortcuts import render
from .models import Room
# Create your views here.


def home(request):
    return render(request, 'base/home.html')


def about(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/room.html', context)


def aboutdetail(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/single-room.html', context)
