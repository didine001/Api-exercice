from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from server import app


client = TestClient(app)


def test_search_artists_valid_name():
    artist_name = "Accept"
    response = client.get(f"/artists/{artist_name}")
    assert response.status_code == 200

def test_search_artists_not_valid_name():
    artist_name = "Halliday"
    response = client.get(f"/artists/{artist_name}")
    assert response.status_code == 404
