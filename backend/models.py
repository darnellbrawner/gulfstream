from sqlalchemy import Boolean, Column, Integer, String, REAL, ForeignKey
from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import relationship

from database import Base

class Base(DeclarativeBase):
    pass
    __allow_unmapped__ = True

class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    
    avionics = relationship("Avionic", back_populates="manufacturer")
    engines = relationship("Engine", back_populates="manufacturer")
    windows = relationship("Window", back_populates="manufacturer")

class Window(Base):
      __tablename__ = 'windows'
      id = Column(Integer, primary_key=True, index=True)
      size = Column(String)
      shape = Column(String)
      panoramic = Column(Boolean, default=True)
      manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))
      manufacturer = relationship("Manufacturer", back_populates="windows")

      planes = relationship("Plane", back_populates="window")


class Avionic(Base):
    __tablename__ = 'avionics'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id") ) 
    manufacturer = relationship("Manufacturer", back_populates="avionics")    
    
    planes = relationship("Plane", back_populates="avionic")

class Engine(Base):
    __tablename__ = 'engines'
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String)
    model = Column(String)
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id") ) 
    manufacturer = relationship("Manufacturer", back_populates="engines")  
    
    planes = relationship("Plane", back_populates="engine")

class Plane(Base):
    __tablename__ = "planes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    max_range = Column(Integer,nullable=True)
    max_range_unit = Column(String,nullable=False)
    high_speed_cruise = Column(REAL, nullable=True)
    long_range_cruise = Column(REAL, nullable=True)
    cruising_unit = Column(String, nullable=False)
    #Cabin
    living_areas_max = Column(REAL)
    window_count = Column(Integer)
    window_id = Column(Integer, ForeignKey("windows.id") )
    total_interior_length = Column(Integer)
    interior_length_unit = Column(String)
    #Systems
    avionic_id = Column(Integer, ForeignKey("avionics.id") )
    engine_id = Column(Integer, ForeignKey("engines.id") )
    engine_count = Column(Integer)
    delivered = Column(Boolean, default=False)

    window = relationship("Window", back_populates="planes")

    engine = relationship("Engine", back_populates="planes")
    avionic = relationship("Avionic", back_populates="planes")
#,link_to_name=True