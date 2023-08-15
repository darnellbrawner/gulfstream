from .base_model import *

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