import datetime

class SpotifyAPI(object):
    access_token = None
    access_expiration = datetime.datetime.now()
    client_id = None
    client_secret = None

    def __init__ (self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)