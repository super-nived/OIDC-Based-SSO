from django.shortcuts import render
from .models import *
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from jose import jwt
import requests

@login_required
def home(request):
    user_profile = UserProfileA.objects.get(username=request.user.username)
    return HttpResponse(f"Welcome to Service A, {user_profile.username}!")

def login(request):
    redirect_uri = f"{AUTH0_CALLBACK_URL}/callback"
    auth_url = (
        f"https://{AUTH0_DOMAIN}/authorize?"
        f"response_type=code&client_id={AUTH0_CLIENT_ID}&"
        f"redirect_uri={redirect_uri}&scope=openid profile email"
    )
    return HttpResponseRedirect(auth_url)

@login_required
def callback(request):
    auth0_domain = settings.AUTH0_DOMAIN
    auth0_client_id = settings.AUTH0_CLIENT_ID
    auth0_client_secret = settings.AUTH0_CLIENT_SECRET
    auth0_callback_url = settings.AUTH0_CALLBACK_URL

    code = request.GET.get('code')

    # Exchange the code for an access token
    token_url = f'https://{auth0_domain}/oauth/token'
    token_payload = {
        'grant_type': 'authorization_code',
        'client_id': auth0_client_id,
        'client_secret': auth0_client_secret,
        'code': code,
        'redirect_uri': auth0_callback_url,
    }
    token_response = requests.post(token_url, data=token_payload)
    token_data = token_response.json()
    access_token = token_data.get('access_token')

    # Decode the ID token to get user information
    id_token = token_data.get('id_token')
    decoded_id_token = jwt.decode(id_token, algorithms=['RS256'], issuer=f'https://{auth0_domain}/', audience=auth0_client_id)

    # Save the user profile in the database
    user_profile, created = UserProfileA.objects.get_or_create(username=decoded_id_token.get('sub'))

    # Redirect to the home page
    return HttpResponseRedirect('/service_a/')


@login_required
def protected_resource(request):
    user_id = request.user.id
    jwt_token = jwt.encode({'user_id': user_id}, settings.JWT_RSA_PRIVATE_KEY, algorithm=settings.JWT_ALGORITHM)
    return HttpResponse(f"Welcome to Service A. JWT Token: {jwt_token}")