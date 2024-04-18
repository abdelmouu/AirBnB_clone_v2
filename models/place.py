#!/usr/bin/python3

"""Defines the Place class."""

from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
<<<<<<< HEAD
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
=======
    """Represents a place in the application.

    Attributes:
        city_id (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of
        guests the place can accommodate.
        price_by_night (int): The price per night for staying at the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        reviews (relationship): Relationship with the Review model.
        Includes cascade delete to delete associated reviews.
        amenities (relationship): Relationship with the Amenity
        model through a many-to-many table.
        Includes a backref to access places associated
        with each amenity.
>>>>>>> b037452f67be4e587df226ba99a895be5d5b4980
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False, backref="places")
    amenity_ids = []

    @property
    def reviews(self):
        """ Returns the list of Review instances with
        place_id == current Review.id """
        list_reviews = []
        place_reviews = models.engine.all(Review)
        for pl_reviews in place_reviews.values():
            if pl_reviews.place_id == self.id:
                list_reviews.append(pl_reviews)
        return list_reviews
<<<<<<< HEAD

=======
>>>>>>> b037452f67be4e587df226ba99a895be5d5b4980
