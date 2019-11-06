from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('discord', views.discord, name='discord'),
    path('discord/callback', views.callback, name='callback'),
    path('dashboard', views.dashboard, name='dashboard')
]