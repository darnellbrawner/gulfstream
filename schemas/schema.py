from datetime import datetime
from typing import List
from pydantic import BaseModel
from typing import Optional

class MyBaseModel(BaseModel):
    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True