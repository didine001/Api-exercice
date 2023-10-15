from fastapi import FastAPI, HTTPException
from .database import SessionLocal
from fastapi import Depends
from . import models

app = FastAPI()

# Dépendance pour la gestion de la session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/genres/")
def read_genres(db: SessionLocal=Depends(get_db)):
    """
    Récupère la liste des genres depuis la base de données.
    """
    genres = db.query(models.Genres).all()
    return genres

@app.get("/artists/{name}")
async def get_artists_by_name(name: str,db: SessionLocal=Depends(get_db)):
    """
    Récupère la liste d'artistes dont le nom contient la chaîne donnée.
    """
    artists = db.query(models.Artists).filter(models.Artists.Name.like(f"%{name}%")).all()
    if(artists):
      return artists
    raise HTTPException(status_code=404, detail="Artists not found")

@app.get("/albums/{id}")
async def get_albums_by_artist_id(id: int, db: SessionLocal= Depends(get_db)):
    """
    Récupère la liste d'albums d'un artiste donné.
    """
    albums = db.query(models.Album).filter(models.Album.ArtistId == id).all()
    if(albums):
        return albums
    raise  HTTPException(status_code=404, detail="No artist found")

@app.get("/tracks/{id}")
async def get_track_name_by_album_id(id: int, db: SessionLocal= Depends(get_db)):
    """
    Récupère la liste des titres d'un album donné.
    """
    track = db.query(models.Track).filter(models.Track.AlbumId == id).all()
    if(track):
        return track
    raise  HTTPException(status_code=404, detail="No album found")