from os import getenv
import requests

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponse
from dotenv import load_dotenv
load_dotenv()


class Home(TemplateView):
    template_name = 'home/index.html'


class Dashboard(TemplateView):
    template_name = 'home/dashboard.html'


class Faq(TemplateView):
    template_name = 'home/faq.html'
