from fastapi import FastAPI, HTTPException
from .database import SessionLocal
from fastapi import Depends
from . import models

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/genres/")
def read_genres(db: SessionLocal=Depends(get_db)):
    genres = db.query(models.Genres).all()
    return genres

@app.get("/artists/{name}")
async def get_artists_by_name(name: str,db: SessionLocal=Depends(get_db)):
    artists = db.query(models.Artists).filter(models.Artists.Name.like(f"%{name}%")).all()
    if(artists):
      return artists
    raise HTTPException(status_code=404, detail="Artists not found")

@app.get("/artists/{id}")
async def get_albums_by_artist_id(id: int, db: SessionLocal= Depends(get_db)):
    albums = db.query(models.Album).filter(models.Album.ArtistId == id).first()
    if(albums):
        return albums
    raise  HTTPException(status_code=404, detail="No artist found")