from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('dashboard', views.Dashboard.as_view(), name='dashboard'),
    path('faq', views.Faq.as_view(), name='faq')
]