import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters' 
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250))
    skin_color = Column(String(250))
    birth_year = Column(String(250))
    created = Column(String(250))
    mass = Column(Integer)
    height = Column(Integer)
    homeworld = Column(String(250), ForeignKey('planets.id'))
    specie = Column(String(250), ForeignKey("specie.id"))


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250),  nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    terrain = Column(String(250))
    climate = Column(String(250))
    surface_water = Column(Integer)
    created = Column(Integer)
    population = Column(Integer)
    aircraft_belonging = Column(String(250), ForeignKey('starships.id'))
    vehicle_belonging = Column(String(250), ForeignKey('vehicle.id'))
    characters = relationship(Characters)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    velocity = Column(Integer)
    pilot = Column(Integer, ForeignKey('characters.id')) 
    created = Column(Integer)
    model = Column(String(250), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    velocity = Column(Integer)
    pilot = Column(Integer, ForeignKey('characters.id')) 
    created = Column(Integer)
    model = Column(String(250), nullable=False)

class Specie(Base):
    __tablename__ = "specie"
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    classification = Column(String(250))
    designation = Column(String(250))
    language = Column(String(250))
    characters = relationship(Characters)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')