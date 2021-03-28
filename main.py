import responses
import requests
import json
import pandas as pd
from secrets import spotify_access_token, spotify_user_name
   
SPOTIFY_CREATE_PLAYLIST_URL = f'https://api.spotify.com/v1/users/{spotify_user_name}/playlists'
PLAYLIST_ITEM = 'https://api.spotify.com/v1/playlists/5e8ijEDzlaB0y9apSoZNBI/tracks'


def create_playlist_on_spotify(name, public):
    responses = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {spotify_access_token}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = responses.json()
    return json_resp

def get_top_artists():
    url = "https://api.spotify.com/v1/me/top/artists"
    responses = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {spotify_access_token}"
        }
    )
    json_resp = responses.json()
    print(json.dumps(json_resp, indent = 3))
    #return json_resp


def user_top_tracks():
    url = "https://api.spotify.com/v1/me/top/tracks"
    responses = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {spotify_access_token}"
        }
    )
    json_resp = responses.json()
    print(json.dumps(json_resp, indent = 3))
    #return json_resp

def get_recommendation():
    url = "https://api.spotify.com/v1/recommendations?limit=3&market=IS&seed_artists=0MtTfq27LQu7CmE5t308Up&seed_tracks=0c6xIDDpzE81m2q797ordA&min_energy=0.4&min_popularity=50"
    responses = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {spotify_access_token}"
        }
    )
    json_resp = responses.json()
    print(json.dumps(json_resp, indent = 3))
    #return json_resp

#TODO: Get top <X(10)> artist of user
# get recommendations tracks/other_artists from them
# if multiple top artist have same recommended track/other_artist then recommend to user

def get_recommendation_from_artist(artist_id, country_code):
    # bubbi_id = 0MtTfq27LQu7CmE5t308Up
    # https://developer.spotify.com/console/get-recommendations/
    url = f"https://api.spotify.com/v1/recommendations?market={country_code}&seed_artists={artist_id}"
    responses = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {spotify_access_token}"
        }
    )
    json_resp = responses.json()
    with open(f'data/recommendations_from_{artist_id}.json', 'w') as f:
        json.dump(json_resp, f, ensure_ascii=False)
    #return json_resp

def main():
    #playlist = create_playlist_on_spotify(name="Big Data Rules!", public=False)
    #get_top_artist = get_top_artists()
    #top_tracks = user_top_tracks()
    #get_recommendation()
    get_recommendation_from_artist("0MtTfq27LQu7CmE5t308Up", "IS")
    #get_top_artists()
    
    #print(f"top artists: {get_top_artists}")
    #print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()