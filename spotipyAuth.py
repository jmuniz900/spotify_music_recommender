import os                                   #Basic Operating System Library
import sys                                  #
import json                                 #For encoding/decoding JSON files
import webbrowser                           #To be able to use web browser functionalities
import mysql.connector                      #To create, store, and pick up sql database items
from mysql.connector import errorcode
import spotipy.util as util                 #
from json.decoder import JSONDecodeError    #
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

userSongPlaying = spotifyObject.current_user_playing_track() #returns a json dump of data

#print(json.dumps(userSongPlaying, sort_keys=True, indent=4))
#print(json.dumps(VARIABLE, sort_keys=True, indent=4)) <----- format for all the info

songName = userSongPlaying['item']['name'] #returns the song name 
#songGenres = userSongPlaying['genres']
songArtist = userSongPlaying['item']['artists']

for info in songArtist:
    print(info['name'])

print(songName) #<--- this works

#print(songGenres)
#print(songArtist)

#Next, we put this information into an sql
try:
    musicDatabase = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password"
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Username or password is wrong!")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist!")
    else:
        print(err)
else:
    print(musicDatabase)
