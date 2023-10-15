from sqlalchemy import  Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Artists(Base):
    __tablename__ = "artists"

    Artistid = Column(Integer, primary_key=True)
    Name = Column(String)

class Genres(Base):
    __tablename__ = "genres"

    Genreid = Column(Integer, primary_key=True)
    Name = Column(String)

class Album(Base):
    __tablename__ = "albums"

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('artists.Artistid')) # L'identifiant de l'artiste associé à l'album.
    Artist = relationship("Artists")

class Track(Base):
    __tablename__ = "tracks"

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    UnitPrice = Column(Integer)
    Composer = Column(String)
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'))
    album = relationship("Album", primaryjoin=AlbumId == Album.AlbumId)  # L'identifiant de l'album auquel la piste est associée.