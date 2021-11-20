from django.shortcuts import render

# Create your views here.

teams = [
    {'id': 1, 'name': 'Dibbya Karki'},
    {'id': 2, 'name': 'Prakash Karki'}
]

about = ['title': 'How we are?', 'description': 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English.']


def home(request):
    return render(request, 'base/home.html')


def about(request):
    context = {'about': about, 'teams': teams}
    return render(request, 'base/about.html', context)


def aboutdetail(request, pk):
    team = None
    for i in teams:
        if(i['id']) == int(pk):
            team = i
    context = {'team': team}
    return render(request, 'base/single-team.html', context)
