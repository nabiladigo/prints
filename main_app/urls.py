from django.urls import path 
from . import views

urlpattrens =[
    path('', views.Home.as_view(), name="home"),
    path('', views.About.as_view(), name="about"),
]