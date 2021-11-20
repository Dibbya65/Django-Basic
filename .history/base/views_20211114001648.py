from django.shortcuts import render

# Create your views here.

team = [
    {'id':1,'name':'Dibbya Karki'},
    {'id':2,'name':'Prakash Karki'}
]

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')
