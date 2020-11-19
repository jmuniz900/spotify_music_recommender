import os
import sys
import json
import webbrowser
import sqlite3
import spotipy.util as util
from json.decoder import JSONDecodeError
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from subprocess import call

#Get username from the terminal
username = sys.argv[1]
scope = "user-read-currently-playing"
"""
windowsPlat = "win32"
linuxPlat = "linux"

if sys.platform is windowsPlat:
    call("./windowsAuth.sh", shell=True)

if sys.platform is linuxPlat:
    call("./linuxAuthen.sh", shell=True)
"""
#https://open.spotify.com/user/dishonesttunic8?si=XPyyy0q3QM-aDJTuLrcu7g
#scope = "user-read-currently-playing"

#Erase cache and prompt user permissions
try:
    token = util.prompt_for_user_token(username, scope)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

#Create the SpotifyObject & collect current playing song.

spotifyObject = spotipy.Spotify(auth=token)
try:
    userSongPlaying = spotifyObject.current_user_playing_track()
except:
    print("Make sure you're playing something on Spotify first before we get started!")

print(json.dumps(userSongPlaying, sort_keys=True, indent=4))
#print(json.dumps(VARIABLE, sort_keys=True, indent=4))

songName = userSongPlaying['item']['name']
#songArtist = userSongPlaying['item']['album']['artists']['name']
print(songName)
#print(songArtist)