from .schema import *

class WindowBaseSchema(BaseModel):
    id: Optional[int]
    name: str
    size: str
    shape: str
    panoramic: bool = True
    manufacturer_id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListWindowResponse(BaseModel):
    status: str
    results: int
    windows: List[WindowBaseSchema]

