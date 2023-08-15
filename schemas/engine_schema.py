from .schema import *

class EngineBaseSchema(BaseModel):
    id: Optional[int]
    make: str
    model: str
    manufacturer_id: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListEngineResponse(BaseModel):
    status: str
    results: int
    egines: List[EngineBaseSchema]

