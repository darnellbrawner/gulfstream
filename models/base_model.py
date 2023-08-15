from .database import Base
from sqlalchemy import Boolean, Column, Integer, String, REAL, ForeignKey, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import get_db

class Base(DeclarativeBase):
     pass
     __allow_unmapped__ = True
