"""
from bottle import route, run, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIPY_CLIENT_ID = '251e552405a74117a5c1448d900fe03b'
SPOTIPY_CLIENT_SECRET = "ed58ab04acef4de7995b78454b82e7e5"
SPOTIPY_REDIRECT_URI = 'https://localhost:8080/'
SCOPE = 'user-read-currently-playing'
CACHE = '.spotipyoauthcache'
#spotify_URI = input("Enter your Spotify URI. This can be found by going to your profile > 3 dots > Share > Copy Spotify URI: ")
#spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

spAuth = spotipy.oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=SCOPE, cache_path=CACHE)

@route('/')
def index():

    access_token = ""

    token_info = spAuth.get_cached_token()
    print(token_info)
    os.system('PAUSE')
    
    if token_info:
        print("Found cached token!")
        access_token = token_info['access_token']
    else:
        url = request.url
        code = spAuth.parse_auth_response_url(url)
        if code:
            print("Found Spotify auth code in Request URL. Trying to get valid access token...")
            token_info = spAuth.get_cached_token()
            access_token = token_info['access_token']

    if access_token:
        print("Access token available. Trying to get user information...")
        sp = spotipy.Spotify(access_token)
        results = sp.current_user()
        return results
    
    else:
        return htmlForLoginButton()

def htmlForLoginButton():
    auth_url = getSPOauthURI()
    htmlLoginButton = "<a href=" + auth_url + ">Login to Spotify</a>"
    return htmlLoginButton

def getSPOauthURI():
    auth_url = spAuth.get_authorize_url()
    return auth_url

run(host='', port=8080)
"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_playback
for idx, item in enumerate(results[])