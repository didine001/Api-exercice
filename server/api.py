from fastapi import FastAPI, HTTPException
from .database import SessionLocal
from fastapi import Depends
from . import models

app = FastAPI()


# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/genres/")
def read_genres(db: SessionLocal = Depends(get_db)):
    """
    Get the list of genres from the database.
    """
    genres = db.query(models.Genres).all()
    return genres


@app.get("/artists/{artist_name}")
async def get_artists_by_name(artist_name: str, db: SessionLocal = Depends(get_db)):
    """
    Get a list of artists whose name contains the given string.
    """
    artists = (
        db.query(models.Artists)
        .filter(models.Artists.Name.like(f"%{artist_name}%"))
        .all()
    )
    if artists:  # If artist_name is found return the artist
        return artists
    raise HTTPException(
        status_code=404, detail="Artists not found"
    )  # Else, we raise exception with status code 404


@app.get("/albums/{artist_id}")
async def get_albums_by_artist_id(artist_id: int, db: SessionLocal = Depends(get_db)):
    """
    Get a list of albums for a given artist.
    """
    albums = db.query(models.Album).filter(models.Album.ArtistId == artist_id).all()
    if albums:
        return albums
    raise HTTPException(status_code=404, detail="No artist found")


@app.get("/tracks/{album_id}")
async def get_track_name_by_album_id(album_id: int, db: SessionLocal = Depends(get_db)):
    """
    Get a list of titles for a given album.
    """
    track = db.query(models.Track).filter(models.Track.AlbumId == album_id).all()
    if track:
        return track
    raise HTTPException(status_code=404, detail="No album found")


@app.delete("/artists/{artist_id}")
async def delete_artist(artist_id: int, db: SessionLocal = Depends(get_db)):
    """
    Delete an artist by their ID.
    """
    artist = (
        db.query(models.Artists).filter(models.Artists.Artistid == artist_id).first()
    )
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")

    db.delete(artist)
    db.commit()

    return {"Artist deleted successfully"}


@app.put("/artists/{artist_id}")
async def update_artist_name(
    artist_id: int, name: str, db: SessionLocal = Depends(get_db)
):
    """
    Update the name of an artist by their ID.
    """
    artist = db.query(models.Artists).filter(models.Artists.Artistid == artist_id).first()
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")

    artist.Name = name

    db.commit()
    db.refresh(artist)

    return artist
