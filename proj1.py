import requests
import sys
import os

import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.cache_handler import FlaskSessionCacheHandler

from dotenv import load_dotenv

from flask import Flask, session


load_dotenv() # loads in environment variables from .env file

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') # get secret key from .env file

redirect_url = 'https://www.example.com/callback' # same URL entered in spotify deve app settings
scope = "user-library-read, user-top-read" # what data we want to read from users spotify

cache_handler = FlaskSessionCacheHandler(session) # Flask session cache handler to store access tokens

# Initialize Spotify client with OAuth (This allows us to access user data)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = os.getenv('SPOTIPY_CLIENT_ID'),
                                               client_secret = os.getenv('SPOTIPY_CLIENT_SECRET'),
                                               redirect_uri = redirect_url,
                                               scope = scope,
                                               cache_handler = cache_handler,
                                               swhow_dialog = True,)
                                               )

if __name__ == '__main__':
    app.run(debug=True)
