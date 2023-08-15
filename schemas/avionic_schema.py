from .schema import *

class AvionicBaseSchema(BaseModel):
    id: Optional[int]
    name: str
    manufacturer_id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class ListAvionicResponse(BaseModel):
    status: str
    results: int
    avionics: List[AvionicBaseSchema]

