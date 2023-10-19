import requests

FAST_API_URL = "http://127.0.0.1:8000"


def search_artists_by_name(artist_name):
    response = requests.get(
        f"{FAST_API_URL}/artists/{artist_name}"
    )  # we use the endpoint created in api.py and we use the corresponding route to get the data.
    return (
        response.json()
    )  # We format on json because if we don't it returns an object.


def read_genres():
    response = requests.get(f"{FAST_API_URL}/genres/")
    return response.json()


def get_albums_by_artist_id(artist_id):
    response = requests.get(f"{FAST_API_URL}/albums/{artist_id}")
    return response.json()


def get_track_name_by_album_id(album_id):
    response = requests.get(f"{FAST_API_URL}/tracks/{album_id}")
    return response.json()
