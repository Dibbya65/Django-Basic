from django.shortcuts import render

# Create your views here.

teams = [
    {'id': 1, 'name': 'Dibbya Karki'},
    {'id': 2, 'name': 'Prakash Karki'}
]


def home(request):
    return render(request, 'base/home.html')


def about(request, pk):
    context = {'teams': teams}
    return render(request, 'base/about.html', context)
