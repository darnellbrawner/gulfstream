from .schema import *

class AvionicBaseSchema(MyBaseModel):
    id: Optional[int]
    name: str
    manufacturer_id: int


class ListAvionicResponse(MyBaseModel):
    status: str
    results: int
    avionics: List[AvionicBaseSchema]

