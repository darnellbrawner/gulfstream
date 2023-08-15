from .base_model import *

class Avionic(Base):
    __tablename__ = 'avionics'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id") ) 
    manufacturer = relationship("Manufacturer", back_populates="avionics")    
    
    planes = relationship("Plane", back_populates="avionic")