import requests
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

if len(sys.argv) < 1:
    print("Please input a valid url")
    sys.exit()

url_Artist = 

print(f"Name: {data_artist['name']}")

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
artist = sp.artist(token)
response = sp.artist_top_tracks(url_Artist)

for track in response['tracks']:
    print(track['name'])






