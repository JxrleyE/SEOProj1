# **NEEDS UPDATE**

# SPOTIFY API PROJECT

  This project demonstrates basic interaction with the Spotify Web API
  using two different approaches to receive information like artist data,
  and top tracks

## **INSTRUCTIONS** 📝

### _Prerequisites_ 

* Python 3.x
* Install the following libraries: requests, spotipy, pandas, sqlalchemy
> Quick note: If using the Spotipy library(Shown in 'methodBranch')
> you **NEED** to register a Spotify developer app to get your Client ID
> and Client Secret
>> sign up here: [Spotify For Developers][https://developer.spotify.com/]


### *Environmental Variables*

If you're using Spotipy:
* export SPOTIPY_CLIENT_ID='your-client-id'
* export SPOTIPY_CLIENT_SECRET='your-client-secret'


### How To Run Code ‼️

** If not using spotipy, use your Client ID and Secret to make a TOKEN **

Paste the following in your terminal and replace the ID and Secret with yours:

curl -X POST "https://accounts.spotify.com/api/token" \
-H "Content-Type: application/x-www-form-urlencoded" \ 
-d "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"


## *Master Branch* 
Runs a GET request with token and artist ID
* python3 proj1.py TOKEN_HERE ID_OF_ARTIST

## *API-Data-Into-DB-Branch*
Gets Spotify API data and saves it into a local SQLite DB with token and artist ID:
* python3 proj1.py TOKEN_HERE ID_OF_ARTIST

## *MethodBranch (spotipy)*
Uses the spotipy library and a command-line argument to get top tracks for a given artist URL:

* python3 proj1.py spotify:artist:3jOstUTkEu2JkjvRdBA5Gu

>There are 3 different ways to give a URL, See here:
[Spotipy Doc][https://spotipy.readthedocs.io/en/2.25.1/]