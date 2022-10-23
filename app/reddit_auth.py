import requests
import os
from dotenv import load_dotenv

def get_auth_headers():
    load_dotenv()

    CLIENT_ID = os.getenv("CLIENT_ID")
    SECRET_TOKEN = os.getenv("SECRET_TOKEN")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")


    # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

    # here we pass our login method (password), username, and password
    data = {'grant_type': 'password',
            'username': USERNAME,
            'password': PASSWORD}

    # setup our header info, which gives reddit a brief description of our app
    headers = {'User-Agent': 'MyBot/0.0.1'}

    # send our request for an OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    # convert response to JSON and pull access_token value
    TOKEN = res.json()['access_token']

    # add authorization to our headers dictionary
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    
    return headers
