from sqlalchemy import Column, ForeignKey, Integer, String
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
    ArtistId = Column(Integer, ForeignKey("artists.Artistid"))
    Artist = relationship("Artists")  # Identifies the artist associated with the album.


class Track(Base):
    __tablename__ = "tracks"

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    UnitPrice = Column(Integer)
    Composer = Column(String)
    AlbumId = Column(Integer, ForeignKey("albums.AlbumId"))
    album = relationship(
        "Album", primaryjoin=AlbumId == Album.AlbumId
    )  # Identifies the album to which the track is associated.


class Customers(Base):
    __tablename__ = "customers"

    CustomerId = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)
    Country = Column(String)


class Invoices(Base):
    __tablename__ = "invoices"

    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(Integer, ForeignKey("customers.CustomerId"))
    custom = relationship(
        "Customers", primaryjoin=CustomerId == Customers.CustomerId
    )  # Relates invoices to customers.


class Invoice_items(Base):
    __tablename__ = "invoice_items"

    InvoiceItemId = Column(Integer, primary_key=True)
    InvoiceId = Column(Integer, ForeignKey("invoices.InvoiceId"))
    TrackId = Column(Integer, ForeignKey("tracks.TrackId"))
    custom = relationship(
        "Invoices", primaryjoin=InvoiceId == Invoices.InvoiceId
    )  # Relates invoice items to invoices.
