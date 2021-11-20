from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('about/<str:pk>', views.aboutdetail, name="about-detail"),
]
