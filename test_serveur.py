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


def test_delete_artist():
    artist_id = "258"
    response = client.delete(f"/artists/{artist_id}")
    assert response.status_code == 200


def test_delete_artist_invalid():
    artist_id = "5070"
    response = client.delete(f"/artists/{artist_id}")
    assert response.status_code == 404


def test_update_artist_name():
    artist_id = "55"
    new_name = "The weeknd"
    response = client.put(f"/artists/{artist_id}?name={new_name}")
    assert response.status_code == 200


def test_update_artist_name_invalid():
    artist_id = "9999"
    new_name = "John"
    response = client.put(f"/artists/{artist_id}?name={new_name}")
    assert response.status_code == 404


def test_create_artist():
    new_name = "the jones"
    response = client.post(f"/artists/?new_name={new_name}")
    assert response.status_code == 200

def test_create_artist_invalid():
    new_name = "weekendes"
    response = client.post(f"/artists/?new_name={new_name}")
    assert response.status_code == 404