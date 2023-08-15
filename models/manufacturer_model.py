from .base_model import *

class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    
    avionics = relationship("Avionic", back_populates="manufacturer")
    engines = relationship("Engine", back_populates="manufacturer")
    windows = relationship("Window", back_populates="manufacturer")
