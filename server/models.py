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
    ArtistId = Column(Integer, ForeignKey('artists.Artistid'))
    artist = relationship("Artists")