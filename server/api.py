from fastapi import FastAPI, HTTPException
from sqlalchemy import func
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

@app.get("/top_tracks/")
async def get_top_tracks(db: SessionLocal = Depends(get_db)):
    """
    Get the top tracks based on the number of customers who have purchased them.
    """
    top_tracks = (
        db.query(
            models.Track.Name,
            func.count(models.Invoices.CustomerId).label(
                "customer_count"
            ),  # Count the number of customers
        )
        .join(
            models.Invoice_items, models.Invoice_items.TrackId == models.Track.TrackId
        )
        .join(
            models.Invoices, models.Invoices.InvoiceId == models.Invoice_items.InvoiceId
        )
        .group_by(models.Track.Name)
        .order_by(func.count(models.Invoices.CustomerId).desc())
        .limit(3)
        .all()
    )
    top_tracks_data = [
        {"TrackName": name, "CustomerCount": count}
        for name, count in top_tracks  # Formatting the objects
    ]
    if top_tracks:
        return top_tracks_data
    else:
        raise HTTPException(status_code=404, detail="No top tracks found")
