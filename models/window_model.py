from .base_model import *

class Window(Base):
      __tablename__ = 'windows'
      id = Column(Integer, primary_key=True, index=True)
      size = Column(String)
      shape = Column(String)
      panoramic = Column(Boolean, default=True)
      manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))
      manufacturer = relationship("Manufacturer", back_populates="windows")

      planes = relationship("Plane", back_populates="window")