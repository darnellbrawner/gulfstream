from .base_model import *

class Engine(Base):
    __tablename__ = 'engines'
    id = Column(Integer, primary_key=True, index=True)
    make = Column(String)
    model = Column(String)
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id") ) 
    manufacturer = relationship("Manufacturer", back_populates="engines")  
    
    planes = relationship("Plane", back_populates="engine")