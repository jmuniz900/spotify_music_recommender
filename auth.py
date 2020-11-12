import base64
import requests
import datetime

client_id = "251e552405a74117a5c1448d900fe03b"
client_secret = "0999753d6a6245c6a04c1b563fba1020"

token_url = "https://accounts.spotify.com/api/token"
method = "POST"

client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode())
#print(client_creds_b64)

#base64.b64decode(client_creds_b64)
#type(client_creds)

token_data = {
    "grant_type": "client_credentials"
}
token_header = {
    "Authorization": f"Basic {client_creds_b64.decode()}" #<base64 encoded client_id:client_secret>
}

r = requests.post(token_url, data = token_data, headers = token_header)
valid_request = r.status_code in range(200, 299)
#print(r.json())
token_response_data = r.json()

dateNow = datetime.datetime.now()
access_token = token_response_data['access_token']
expires_in = token_response_data['expires_in'] #in seconds <---3600 sec = 1 hr
expires = dateNow + datetime.timedelta(seconds=expires_in) #adds an hour to the current date, to say what time it expires in on what day
#print(expires)
expiredValue = dateNow > expires #Gives true or false values whether the token expired or not
#print(expiredValue)