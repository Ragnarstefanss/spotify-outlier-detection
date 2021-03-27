import responses
import requests
import json
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
    ARTISTS = "https://api.spotify.com/v1/me/top/artists"
    responses = requests.get(
        ARTISTS,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {spotify_access_token}"
        }
    )
    json_resp = responses.json()
    print(json.dumps(json_resp, indent = 3))
    #return json_resp

def main():
    playlist = create_playlist_on_spotify(
        name="Big Data Rules!",
        public=False
    )
    
    get_top_artist = get_top_artists()
    get_top_artists()
    #print(f"top artists: {get_top_artists}")
    #print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()