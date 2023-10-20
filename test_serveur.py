from fastapi.testclient import TestClient
from server import app


client = TestClient(app)


def test_read_genres():
    response = client.get("/genres/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_search_artists_by_name():
    artist_name = "Accept"
    response = client.get(f"/artists/{artist_name}")
    assert response.status_code == 200
    expected_data = {"Artistid": 2, "Name": "Accept"}
    assert expected_data in response.json()


def test_search_artists_not_valid_name():
    artist_name = "Halliday"
    response = client.get(f"/artists/{artist_name}")
    assert response.status_code == 404


def test_search_artists_not_found():
    artist_name = "ArtistUnknown"

    response = client.get(f"/artists/{artist_name}")
    assert response.status_code == 404


def test_get_track_name_by_album_id():
    album_id = "5"
    response = client.get(f"/tracks/{album_id}")
    assert response.status_code == 200


def test_get_track_name_by_album_id_invalid():
    album_id = "1000"
    response = client.get(f"/tracks/{album_id}")
    assert response.status_code == 404

def test_get_album_by_artist_id():
    artist_id = "2"
    response = client.get(f"/tracks/{artist_id}")
    assert response.status_code == 200

def test_get_album_by_artist_id_invalid():
    artist_id = "2000"
    response = client.get(f"/tracks/{artist_id}")
    assert response.status_code == 404