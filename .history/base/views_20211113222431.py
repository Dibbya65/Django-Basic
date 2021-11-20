from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(reqeust):
    return HttpResponse('Home Page')


def about(reqeust):
    return HttpResponse('This is a about page')
