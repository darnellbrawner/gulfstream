from .schema import *

class WindowBaseSchema(MyBaseModel):
    id: Optional[int]
    name: str
    size: str
    shape: str
    panoramic: bool = True
    manufacturer_id: int

class ListWindowResponse(MyBaseModel):
    status: str
    results: int
    windows: List[WindowBaseSchema]

