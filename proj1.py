import requests
import sys
import os

import spotipy
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

from dotenv import load_dotenv

from flask import Flask, session, url_for, redirect, request


load_dotenv() # loads in environment variables from .env file

app = Flask(__name__)
app.config['SECRET_KEY'] = '5470be5cacb6a0728151e0be12270d26'

redirect_uri = 'https://phoneapril-yogatouch-4000.codio.io/proxy/5000/callback' # same URI entered in spotify deve app settings
scope = "user-top-read" # what data we want to read from users spotify

cache_handler = FlaskSessionCacheHandler(session) # Flask session cache handler to store access tokens

# Initialize Spotify client with OAuth (This allows us to access user data)
auth_manager = SpotifyOAuth(client_id = os.getenv('CLIENT_ID'),
                                               client_secret = os.getenv('CLIENT_SECRET'),
                                               redirect_uri = redirect_uri,
                                               scope = scope,
                                               cache_handler = cache_handler,
                                               show_dialog = True)

sp = spotipy.Spotify(auth_manager= auth_manager)

# Login page
@app.route('/')
def login():
    # If user isnt logged in send them to Spotify login page
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        auth_url = auth_manager.get_authorize_url() 
        return redirect(auth_url) # Redirect to login 
    return redirect(url_for('home')) # Redirect user to home page if already logged in 

@app.route('/callback')
def callback():
    auth_manager.get_access_token(request.args['code'])  # Get the access token after user has logged in
    return redirect(url_for('home'))

# Home page
@app.route('/home')
def home():
     # If user isnt logged in send them to Spotify login page
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        auth_url = auth_manager.get_authorize_url() 
        return redirect(auth_url) # Redirect to login 
    
    # DISPLAY WELCOME MESSAGE ALONG WITH CHOICES 
    user_info = sp.current_user()
    user_name = user_info['display_name']

    ##CALL HOME TEMPLATE

    return redirect(url_for('top_artists'))  

# Top tracks page
@app.route('/top_tracks')
def top_tracks():
    # If user isnt logged in send them to Spotify login page
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        auth_url = auth_manager.get_authorize_url() 
        return redirect(auth_url) # Redirect to login 
    
    # Get the user's top tracks
    sp_top_tracks = sp.current_user_top_tracks(limit=48, time_range='medium_term')

    # Extract track names and artists
    top_tracks_list = []
    for item in sp_top_tracks['items']:
        track_info = {
            'name': item['name'],
            'artists': ', '.join(artist['name'] for artist in item['artists']),
            'album': item['album']['name'],
            'url': item['external_urls']['spotify']
        }
        top_tracks_list.append(track_info)

# Top artits page
@app.route('/top_artists')
def top_artists():
     # If user isnt logged in send them to Spotify login page
    if not auth_manager.validate_token(cache_handler.get_cached_token()):
        auth_url = auth_manager.get_authorize_url() 
        return redirect(auth_url) # Redirect to login 
    
    # Get the user's top albums
    sp_top_albums = sp.current_user_top_artists(limit=48, time_range='medium_term')

    # Extract top artists
    top_artists_list = []
    for item in sp_top_albums['items']:
        artist_info = {
            'name': item['name'],
            'genres': ', '.join(item['genres']),
            'url': item['external_urls']['spotify']
        }
        top_artists_list.append(artist_info)
    
    return top_artists_list

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
