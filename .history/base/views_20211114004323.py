from django.shortcuts import render

# Create your views here.

teams = [
    {'id': 1, 'name': 'Dibbya Karki'},
    {'id': 2, 'name': 'Prakash Karki'}
]


def home(request):
    return render(request, 'base/home.html')


def about(request):
    context = {'teams': teams}
    return render(request, 'base/about.html', context)


def aboutdetail(request, pk):
    for i in teams:
        if(i['id']) == int(pk):
            team = i
    context = {'team': team}
    return render(request, 'base/single-team.html', context)
