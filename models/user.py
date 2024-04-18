#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """Represents a user in the application.

    Attributes:
        email (str): The email address of the user.
        password (str): The password for user login.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        places (relationship): Relationship with the Place model.
        Includes cascade delete to delete associated places.
        reviews (relationship): Relationship with the Review model.
        Includes cascade delete to delete associated reviews.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade="all, delete", backref="user")
    reviews = relationship("Review", cascade="all, delete", backref="user")
