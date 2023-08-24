from .schema import *

class EngineBaseSchema(MyBaseModel):
    id: Optional[int]
    make: str
    model: str
    manufacturer_id: int


class ListEngineResponse(MyBaseModel):
    status: str
    results: int
    egines: List[EngineBaseSchema]

