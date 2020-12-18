import os                                   #Basic Operating System Library
import sys                                  #Python System Manipulation Tools
import json                                 #For encoding/decoding JSON files
import webbrowser                           #To be able to use web browser functionalities
import spotipy.util as util                 #Use utilities in spotipy
from json.decoder import JSONDecodeError    #Dissect json data files
import spotipy                              #spotipy library for Spotify API usage
from spotipy.oauth2 import SpotifyOAuth     #Spotify Authentication Library
from spotipy.oauth2 import SpotifyClientCredentials #Spotify Credential Library

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

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

#Create the SpotifyObject & collect current playing song.

spotifyObject = spotipy.Spotify(auth=token)

userSongPlaying = spotifyObject.current_user_playing_track() #returns a json dump of data

#print(json.dumps(userSongPlaying, sort_keys=True, indent=4))
#print(json.dumps(VARIABLE, sort_keys=True, indent=4)) <----- format for all the info

response= True
while(response):
    try:
        songList = []           #Empty list of song IDs
        artistList = []         #Empty list of artist IDs
        songName = userSongPlaying['item']['name'] #returns the song name 
        #songGenres = userSongPlaying['genres']
        songArtist = userSongPlaying['item']['artists']
        songID = userSongPlaying['item']['id']
        songList.append(songID)

        for info in songArtist:
            #print(info['name'])
            artistID = info['id']
            artistList.append(artistID)

        #print(artistID)
        print("Recommendations for", songName)
        #print(songID)
        #print(songGenres)
        #print(songArtist)

        '''
        genres = sp.recommendation_genre_seeds()
        print(json.dumps(genres, sort_keys=True, indent=4))
        '''
        #Loop around the recommendations to print the list
        def show_recommendations_for_songs(songID):
            results = sp.recommendations(seed_tracks=songID)
            for track in results['tracks']:
                print('Recommendation:', track['name'],' - ', track['artists'][0]['name'])

        show_recommendations_for_songs(songList)

        userAns = input("Do you want to reroll the songs?  ")
        try:
            if(userAns == "no" or "No"):
                response = False
        except:
            response = input("Sorry, I don't understand, can you repeat that?")
            if(userAns == "no" or "No"):
                response = False
    #If the user doesn't put in the argument right, add an exception
    except:
        print("User currently not playing a song.")
        print("To start, pass a username currently playing music on Spotify. Example: ")
        print("py spotipyRecommender.py [username]")
        response = False

print("Thanks for using me! Take care. :)")