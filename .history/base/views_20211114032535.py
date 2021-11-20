from django.shortcuts import render
from .models import Team
# Create your views here.


about_page_title = 'How we are?'
about_page_description = 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English.'


def home(request):
    return render(request, 'base/home.html')


def about(request):
    teams = Team.objects.all()
    context = {'about_page_title': about_page_title,
               'about_page_description': about_page_description, 'teams': teams}
    return render(request, 'base/about.html', context)


def aboutdetail(request, pk):
    team = Team.objects.get(id=pk)
    context = {'team': team}
    return render(request, 'base/single-team.html', context)
