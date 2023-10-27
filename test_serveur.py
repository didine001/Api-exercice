from fastapi.testclient import TestClient
from server import app


client = TestClient(app)


# Test reading genres.
def test_read_genres():
    response = client.get("/genres/")
    assert response.status_code == 200
    assert len(response.json()) > 0


# Test searching for artists by name.
def test_search_artists_by_name():
    artist_name = "Accept"
    response = client.get(f"/artists/{artist_name}")
    assert response.status_code == 200
    expected_data = {"Artistid": 2, "Name": "Accept"}
    assert expected_data in response.json()


# Test searching for artists with an invalid name.
def test_search_artists_not_valid_name():
    artist_name = "Halliday"
    response = client.get(f"/artists/{artist_name}")
    assert response.status_code == 404


# Test getting track names by album ID.
def test_get_track_name_by_album_id():
    album_id = "5"
    response = client.get(f"/tracks/{album_id}")
    assert response.status_code == 200


# Test getting track names with an invalid album ID.
def test_get_track_name_by_album_id_invalid():
    album_id = "1000"
    response = client.get(f"/tracks/{album_id}")
    assert response.status_code == 404


# Test getting albums by artist ID.
def test_get_album_by_artist_id():
    artist_id = "2"
    response = client.get(f"/tracks/{artist_id}")
    assert response.status_code == 200


# Test getting albums with an invalid artist ID.
def test_get_album_by_artist_id_invalid():
    artist_id = "2000"
    response = client.get(f"/tracks/{artist_id}")
    assert response.status_code == 404


# Test deleting an artist by ID.
def test_delete_artist():
    artist_id = "258"
    response = client.delete(f"/artists/{artist_id}")
    assert response.status_code == 200


# Test deleting an artist with an invalid ID.
def test_delete_artist_invalid():
    artist_id = "5070"
    response = client.delete(f"/artists/{artist_id}")
    assert response.status_code == 404


# Test updating an artist's name by ID.
def test_update_artist_name():
    artist_id = "55"
    new_name = "The Weeknd"
    response = client.put(f"/artists/{artist_id}?name={new_name}")
    assert response.status_code == 200


# Test updating an artist's name with an invalid ID.
def test_update_artist_name_invalid():
    artist_id = "9999"
    new_name = "John"
    response = client.put(f"/artists/{artist_id}?name={new_name}")
    assert response.status_code == 404


# Test creating a new artist with a valid name.
def test_create_artist():
    new_name = "The Jones"
    response = client.post(f"/artists/?new_name={new_name}")
    assert response.status_code == 200


# Test creating a new artist with an invalid name.
def test_create_artist_invalid():
    new_name = "Weekendes"
    response = client.post(f"/artists/?new_name={new_name}")
    assert response.status_code == 404
