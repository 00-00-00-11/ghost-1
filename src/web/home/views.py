from os import getenv
import requests

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from dotenv import load_dotenv
load_dotenv()


API_ENDPOINT = 'https://discordapp.com/api/v6'
CLIENT_SECRET = getenv('CLIENT_SECRET', None)
CLIENT_ID = getenv('CLIENT_ID', None)
REDIRECT_URI = 'http://127.0.0.1:8000/discord/callback'

# TODO: Refactor into class based views
def index(request):
    return render(request, 'home/index.html')


def discord(request):
    # TODO: Use state in this
    # TODO: Change this for prod
    return redirect(f"https://discordapp.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Fdiscord%2Fcallback&response_type=code&scope=identify%20email")


def callback(request):
    code = request.GET.get('code', 'None')
    if code == 'None':
        return HttpResponse('Missing code')

    response = exchange_code(code)
    user_data = get_user_data(response)
    print(user_data)

    # TODO: Redirect to dashboard
    return redirect('/dashboard')


def dashboard(request):
    return render(request, 'home/dashboard.html')

# Helper functions
# TODO: Split these into a seperate file
def exchange_code(code):
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'scope': 'identify email'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    r = requests.post(f'{API_ENDPOINT}/oauth2/token',
                      data=data, headers=headers)
    return r.json()


def refresh_token(refresh_token):
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'redirect_uri': REDIRECT_URI,
        'scope': 'identify email'
    }
    headers = {
        'Content-Type': 'application/x-www-form-encoded'
    }
    r = requests.post(f'{API_ENDPOINT}/oauth2/token',
                      data=data, headers=headers)
    return r.json()


def get_user_data(resp):
    print(resp)
    access_token = resp['access_token']

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    r = requests.get(f'{API_ENDPOINT}/users/@me', headers=headers)
    return r.json()
