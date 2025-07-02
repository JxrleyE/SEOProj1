import requests
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

if len(sys.argv) < 1:
    print("Please input a valid url")
    sys.exit()

url_Artist = sys.argv[1]

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
artist = sp.artist(url_Artist)
response = sp.artist_top_tracks(url_Artist)

print(artist['name'], ': Here are his top tracks')

for track in response['tracks']:
    print(track['name'])
