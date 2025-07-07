import requests
import sys
import os

import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.cache_handler import FlaskSessionCacheHandler

from dotenv import load_dotenv

from flask import Flask, session, url_form, redirect, request


load_dotenv() # loads in environment variables from .env file

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') # get secret key from .env file

redirect_uri = 'https://www.example.com/callback' # same URI entered in spotify deve app settings
scope = "user-top-read, " # what data we want to read from users spotify

cache_handler = FlaskSessionCacheHandler(session) # Flask session cache handler to store access tokens

# Initialize Spotify client with OAuth (This allows us to access user data)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = os.getenv('SPOTIPY_CLIENT_ID'),
                                               client_secret = os.getenv('SPOTIPY_CLIENT_SECRET'),
                                               redirect_uri = redirect_uri,
                                               scope = scope,
                                               cache_handler = cache_handler,
                                               show_dialog = True)
                                               )

# Login page
@app.route('/')
def login():
    # If user isnt logged in send them to Spotify login page
    if not SpotifyOAuth.validate_token(cache_handler.get_cached_token()):
        auth_url = SpotifyOAuth.get_authorize_url() 
        return redirect(auth_url) # Redirect to login 
    return redirect_url(url_for('home')) # Redirect user to home page if already logged in 

@app.route('/callback')
def callback():
    SpotifyOAuth.get_access_token(request.args['code'])  # Get the access token after user has logged in
    return redirect_url(url_for('home'))


# Home page
@app.route('/home')
def home():
    if not SpotifyOAuth.validate_token(cache_handler.get_cached_token()):  # If we don't have a valid token (user hasnt logged in)
        auth_url = SpotifyOAuth.get_authorize_url()  # Get the authorization URL where users can login 
        return redirect(auth_url) # Redirect to login 
    
    # DISPLAY WELCOME MESSAGE ALONG WITH CHOICES 

    user_info = sp.current_user()

    return user_info
       

if __name__ == '__main__':
    app.run(debug=True)
